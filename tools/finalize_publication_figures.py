"""Post-evaluation figure refinement. No changes to the frozen experiment.

Run finalize_publication_figures(ROOT) in the publication notebook.
Only the six SVG files and their checksum manifest are replaced.
"""
from pathlib import Path
from hashlib import sha256
from xml.sax.saxutils import escape
from xml.etree import ElementTree as ET
from tempfile import TemporaryDirectory
import json
import re
import shutil
import subprocess

INK = '#263238'
MUTED = '#52636A'
GRID = '#E0E6E8'
LIGHT = '#F1F4F5'
ARCH = ('A1', 'A2', 'B1', 'B2', 'C1', 'C2')
COLORS = dict(zip(ARCH, ('#77858B', '#455A64', '#80B0AC', '#367D78', '#90A9C5', '#547DAF')))
LINE_COLORS = dict(zip(ARCH, ('#77858B', '#455A64', '#367D78', '#367D78', '#547DAF', '#547DAF')))
NAMES = ('figure_01_architectures.svg', 'figure_02_experimental_design.svg',
         'figure_03_decision_reliability.svg', 'figure_04_witness_sensitivity.svg',
         'figure_05_conflicting_evidence.svg', 'figure_06_verification_cost.svg')


class SVGFigure:
    def __init__(self, height, title, subtitle):
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img">']
        self.parts.append(f'<title>{escape(title)}</title>')
        self.rect(0, 0, 1000, height, '#FFFFFF')
        self.text(28, 35, title, 24, weight=700)
        self.text(28, 59, subtitle, 14, MUTED)

    def text(self, x, y, value, size=15, color=INK, weight=400, anchor='start'):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(str(value))}</text>')

    def rect(self, x, y, w, h, fill, stroke='none', radius=0):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" rx="{radius}"/>')

    def line(self, x1, y1, x2, y2, color=GRID, width=1, dash=''):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>')

    def polyline(self, points, color, dash=''):
        coordinates = ' '.join(f'{x:.2f},{y:.2f}' for x, y in points)
        self.parts.append(f'<polyline points="{coordinates}" fill="none" stroke="{color}" stroke-width="2.2" stroke-dasharray="{dash}" stroke-linejoin="round"/>')

    def finish(self):
        return ('\n'.join(self.parts + ['</svg>']) + '\n').encode('utf-8')


def rate_panel(fig, x, y, title, rows, step=30):
    """Rows: label, numerator, denominator, color. None = not tested."""
    fig.text(x, y, title, 17, weight=700)
    for i, (label, n, d, color) in enumerate(rows):
        yy = y + 16 + step * i
        fig.text(x, yy + 16, label, 14, weight=600)
        if n is None:
            fig.text(x + 46, yy + 16, 'Not tested', 14, MUTED)
            continue
        fig.rect(x + 46, yy, 230, 20, LIGHT, radius=2)
        fig.rect(x + 46, yy, 230 * n / d, 20, color, radius=2)
        fig.text(x + 285, yy + 16, f'{100*n/d:.1f}% ({n:,}/{d:,})', 14)


def build_figures(data, total_records):
    """Generate deterministic SVGs from the unchanged archived dataset."""
    out = {}
    freeze = data['experimental_freeze']
    sequences = freeze['evaluation_batch_indices']
    ndev = freeze['development_batch_count']
    neval = freeze['evaluation_batch_count']
    metrics = data['evaluation_metrics']
    ncases = len(data['core_results']) // len(ARCH)
    assert len(sequences) == neval and ncases == 1235
    # 1. Shared checks and architecture-specific assurance.
    f = SVGFigure(455, 'Comparative evidence assurance framework',
                  'Six architectures: three verification families, each with and without evidence rules')
    f.rect(100, 81, 800, 70, LIGHT, radius=5)
    f.text(500, 105, 'Common signed evidence and retained verifier history', 19, weight=700, anchor='middle')
    f.text(500, 131, 'Commitment integrity · signature · source authorization · sequence · predecessor', 15, anchor='middle')
    f.line(500, 151, 500, 168, MUTED)
    f.line(180, 168, 820, 168, MUTED)
    families = [('Digital signatures', 'No shared commitment service', 'A1', 'A2'),
                ('Witnessed transparency log', 'Inclusion, consistency, witness quorum', 'B1', 'B2'),
                ('Ethereum anchoring', 'Transaction, event, contract state', 'C1', 'C2')]
    for i, (name, detail, a, b) in enumerate(families):
        x = 28 + i*320
        center = x + 152
        f.line(center, 168, center, 184, MUTED)
        f.rect(x, 184, 304, 65, '#FFFFFF', COLORS[b], 4)
        f.text(center, 209, name, 17, weight=700, anchor='middle')
        f.text(center, 232, detail, 13, anchor='middle')
        f.line(center, 249, center, 261, MUTED)
        f.line(x+73, 261, x+231, 261, MUTED)
        for j, code in enumerate((a, b)):
            xx = x + j*158
            f.line(xx+73, 261, xx+73, 274, MUTED)
            f.rect(xx, 274, 146, 62, '#426B9B' if code == 'C2' else COLORS[code], radius=4)
            fg = '#101820' if j == 0 else '#FFFFFF'
            f.text(xx+73, 299, code, 19, fg, 700, 'middle')
            f.text(xx+73, 320, 'Without rules' if j == 0 else 'With rules', 14, fg, anchor='middle')
            f.line(xx+73, 336, xx+73, 352, MUTED)
        f.line(x+73, 352, x+231, 352, MUTED)
        f.line(center, 352, center, 369, MUTED)
    f.line(180, 369, 820, 369, MUTED)
    f.line(500, 369, 500, 382, MUTED)
    f.rect(180, 382, 640, 47, LIGHT, radius=4)
    f.text(500, 402, 'ACCEPT / REJECT / INDETERMINATE', 17, weight=700, anchor='middle')
    f.text(500, 419, 'Rules cover completeness, freshness, semantics and institutional evidence.', 13, anchor='middle')
    out[NAMES[0]] = f.finish()
    # 2. Chronological partitions; record counts from the verified design / exported data.
    counts = {r['sequence']:r['record_count'] for r in data['batch_latency_results']}
    eval_records = sum(counts.values())
    assert eval_records == freeze['evaluation_record_count']
    # The frozen source partition contains 8,085 referenced records (baseline audit).
    # Derive development count by subtracting the independently counted reserved records.
    dev_records = total_records - eval_records
    f = SVGFigure(340, 'Chronological experimental allocation',
                  'Original batch boundaries preserved; new benchmark commitments and synthetic failures')
    for x, label, count, records, first, last, color in (
        (28, 'Development', ndev, dev_records, 0, ndev-1, COLORS['A2']),
        (508, 'Reserved evaluation', neval, eval_records, sequences[0], sequences[-1], COLORS['B2'])):
        f.rect(x, 89, 464, 102, color, radius=4)
        f.text(x+232, 118, label, 20, '#FFFFFF', 700, 'middle')
        f.text(x+232, 147, f'Batches {first}–{last}  |  {count} batches', 17, '#FFFFFF', anchor='middle')
        f.text(x+232, 174, f'{records:,} original measurement records', 16, '#FFFFFF', anchor='middle')
    f.line(500, 78, 500, 257, MUTED, 1.5, '5 4')
    f.text(260, 221, 'Build and validate the implementations', 16, weight=600, anchor='middle')
    f.text(260, 245, 'Freeze scenarios, reference outcomes and code', 14, anchor='middle')
    f.text(740, 221, f'{len(data["core_results"]):,} core architecture decisions', 16, weight=600, anchor='middle')
    f.text(740, 245, 'Separate robustness and performance experiments', 14, anchor='middle')
    f.text(28, 287, 'The reserved partition is not fully blinded: historical verification inspected all batches.', 14, MUTED)
    f.text(28, 311, 'Repeated scenarios and architectures within a batch are statistically dependent.', 14, MUTED)
    out[NAMES[1]] = f.finish()
    # 3. Decision reliability; numerator and denominator shown for every bar.
    f = SVGFigure(580, 'Comparative decision reliability',
                  f'Reserved evaluation · {ncases:,} cases per architecture · predefined observable-evidence policy')
    for x,y,key in ((28,94,'Decision agreement'),(520,94,'False acceptance'),
                    (28,325,'Violation recognition'),(520,325,'Missing evidence recognition')):
        rows = [(a,*metrics[a][key],COLORS[a]) for a in ARCH]
        rate_panel(f,x,y,key,rows)
    hidden = [metrics[a]['Hidden failure acceptance'] for a in ARCH]
    assert all(n == d for n,d in hidden) and len(set(tuple(v) for v in hidden)) == 1
    n,d = hidden[0]
    f.text(28, 541, f'Hidden pre-commitment alteration and authorized-key compromise: {n}/{d} accepted by every architecture.', 14, MUTED)
    f.text(28, 563, 'Agreement measures policy conformity, not physical truth; violation and missing-evidence rates count components.', 14, MUTED)
    out[NAMES[2]] = f.finish()
    # 4. Witness quorum: distinct experimental denominators.
    f = SVGFigure(352, 'Witness availability and compromise',
                  '3-of-4 witness quorum · separate exhaustive identity-configuration experiments')
    av = data['witness_availability_summary']
    co = data['witness_compromise_summary']
    rate_panel(f,28,96,'A. Checkpoint acceptance',[(r['available'],r['accepted'],r['total'],COLORS['B2']) for r in av])
    rate_panel(f,520,96,'B. Both conflicting checkpoints accepted',[(r['compromised'],r['both_accepted'],r['total'],'#B66A57') for r in co])
    f.text(28, 274, 'Number of available witnesses', 15, weight=600)
    f.text(520, 274, 'Number of compromised witnesses', 15, weight=600)
    f.text(28, 306, 'Primary safety assumption: at most one compromised witness. Acceptance requires three valid votes.', 14, MUTED)
    f.text(28, 330, 'Frequencies describe tested configurations, not real-world attack probabilities.', 14, MUTED)
    out[NAMES[3]] = f.finish()
    # 5. Isolated verifiers: same canonical support versus different local histories.
    f = SVGFigure(365, 'Conflicting evidence across isolated verifiers',
                  'Outcome: both conflicting claims accepted at the same sequence position')
    c = data['conflict_summary']
    rate_panel(f,28,96,'A. Consistent infrastructure (where used)',[(a,c[a]['shared_history_conflicts'],c[a]['total'],COLORS[a]) for a in ARCH])
    rate_panel(f,520,96,'B. Different local blockchain histories',[(a,c[a]['split_chain_conflicts'],c[a]['total'],COLORS[a]) for a in ARCH])
    f.text(28, 306, 'A1/A2 rely on local verifier history only. B1/B2 and C1/C2 use a common canonical commitment.', 14, MUTED)
    f.text(28, 330, 'Panel B tests isolated local chain views, not the security of public Ethereum consensus.', 14, MUTED)
    out[NAMES[4]] = f.finish()
    # 6. All batch-level medians, aggregate quartiles and supporting material.
    f = SVGFigure(740, 'Local verification cost and supporting evidence',
                  '65 reserved control batches · median of five timed runs per batch · local backend queries included')
    lat = data['batch_latency_results']
    by_arch = {a:sorted((r['sequence'],r['median_latency_ms']) for r in lat if r['architecture']==a) for a in ARCH}
    assert all([s for s,_ in v]==sequences for v in by_arch.values())
    x0,x1,y0,y1 = 80,960,116,360
    # Axis maximum is rounded upward to a multiple of 10 ms for readability.
    ymax = 10 * (int(max(v for series in by_arch.values() for _,v in series)/10)+1)
    X = lambda s: x0+(s-sequences[0])/(sequences[-1]-sequences[0])*(x1-x0)
    Y = lambda v: y1-v/ymax*(y1-y0)
    f.text(28, 88, 'A. Verification latency by batch (ms)', 17, weight=700)
    for v in range(0,ymax+1,10):
        y=Y(v); f.line(x0,y,x1,y); f.text(x0-10,y+5,v,13,MUTED,anchor='end')
    f.line(x0,y0,x0,y1,MUTED); f.line(x0,y1,x1,y1,MUTED)
    for s in sorted(set([sequences[0],*range(70,130,10),sequences[-1]])):
        f.text(X(s),y1+19,s,12,MUTED,anchor='middle')
    # Exploratory discontinuity identified in archived data and reproduced by the diagnostic.
    cut = 98.5
    f.line(X(cut),y0,X(cut),y1,'#B66A57',1.6,'5 4')
    f.text(X(cut)+8,y0+14,'98 → 99',13,'#9B4D3B',700)
    for a in ARCH:
        f.polyline([(X(s),Y(v)) for s,v in by_arch[a]],LINE_COLORS[a],'6 4' if a.endswith('1') else '')
    for i,a in enumerate(ARCH):
        x=72+i*148; f.line(x,399,x+28,399,LINE_COLORS[a],2.5,'6 4' if a.endswith('1') else '')
        f.text(x+35,404,a,14,weight=600)
    f.text(28, 431, 'Exploratory diagnostic: transaction and receipt lookup reproduce the transition at 31 → 30 blocks of age.', 13, MUTED)
    f.text(28, 470, 'B. Overall latency (median [Q1, Q3], ms)', 17, weight=700)
    f.text(520,470,'C. Supporting material (median bytes)',17,weight=700)
    lsum=data['latency_summary']; ssum=data['storage_summary']
    lm=max(v['q3'] for v in lsum.values()); sm=max(v['supporting_material_bytes']['median'] for v in ssum.values())
    for i,a in enumerate(ARCH):
        y=488+i*30; l=lsum[a]; b=ssum[a]['supporting_material_bytes']['median']
        f.text(28,y+16,a,14,weight=600)
        f.rect(70,y,180,20,LIGHT,radius=2)
        scale=lambda v:70+180*v/lm
        f.line(scale(l['q1']),y+10,scale(l['q3']),y+10,COLORS[a],5)
        f.line(scale(l['median']),y+2,scale(l['median']),y+18,INK,2)
        f.text(263,y+16,f"{l['median']:.2f} [{l['q1']:.2f}, {l['q3']:.2f}]",14)
        f.text(520,y+16,a,14,weight=600)
        f.rect(562,y,270,20,LIGHT,radius=2); f.rect(562,y,270*b/sm,20,COLORS[a],radius=2)
        f.text(843,y+16,f'{b:,.0f}',14)
    f.text(28, 699, 'Local EthereumTester/Py-EVM behavior; not a public-network performance comparison.', 14, MUTED)
    f.text(28, 721, 'Supporting material excludes the common signed envelope and total infrastructure or network storage.', 14, MUTED)
    out[NAMES[5]] = f.finish()
    for content in out.values():
        assert ET.fromstring(content).tag == '{http://www.w3.org/2000/svg}svg'
    return out


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def read_manifest(text):
    return {name.strip(): h for h,name in (line.split(maxsplit=1) for line in text.splitlines() if line.strip())}


def verify_directory(directory, manifest):
    assert set(manifest) == {'evaluation_results.json', *NAMES}
    assert {p.name for p in directory.iterdir()} == {*manifest, 'SHA256SUMS'}, 'Unexpected files: review manually; nothing deleted.'
    for name, expected in manifest.items():
        assert digest(directory/name) == expected, name


def finalize_publication_figures(root, archive_ref='abff7ab', show=True):
    """Verify, stage, display and replace the six figures; keep one active set."""
    root=Path(root).resolve()
    results=root/'results/reserved_evaluation'
    # The original version is retained in the successful evaluation archive.
    original=read_manifest(subprocess.check_output(['git','show',f'{archive_ref}:results/reserved_evaluation/SHA256SUMS'],cwd=root,text=True))
    current=read_manifest((results/'SHA256SUMS').read_text())
    verify_directory(results,current)
    assert current['evaluation_results.json']==original['evaluation_results.json'], 'Archived scientific data changed.'
    data=json.loads((results/'evaluation_results.json').read_text())
    assert data['experimental_freeze']==json.loads((root/'EVALUATION_FREEZE.json').read_text())
    protocol=root/'PROTOCOL.md'
    assert digest(protocol)==data['experimental_freeze']['document_sha256']['PROTOCOL.md']
    total_records=int(re.search(r"^- ([\d,]+) records referenced by proof metadata$",protocol.read_text(),re.M).group(1).replace(',',''))
    figures=build_figures(data,total_records)
    revised={'evaluation_results.json':current['evaluation_results.json'],**{name:sha256(content).hexdigest() for name,content in figures.items()}}
    assert current in (original,revised), 'Unexpected figure revision: stop rather than overwrite.'
    with TemporaryDirectory(prefix='.publication-',dir=results.parent) as temp:
        temp=Path(temp); stage=temp/'validated'; stage.mkdir()
        shutil.copy2(results/'evaluation_results.json',stage/'evaluation_results.json')
        for name, content in figures.items():
            (stage/name).write_bytes(content)
        (stage/'SHA256SUMS').write_text(''.join(f'{h}  {name}\n' for name,h in sorted(revised.items())),encoding='utf-8')
        verify_directory(stage,revised)
        if show:
            from IPython.display import display, SVG, Markdown
            for name in NAMES:
                display(Markdown('### '+Path(name).stem.replace('_',' ').title()))
                display(SVG(filename=str(stage/name)))
        # Same-filesystem rename with rollback on failure; previous files already in Git.
        if current != revised:
            backup=temp/'previous'; results.rename(backup)
            try:
                stage.rename(results)
                verify_directory(results,revised)
            except BaseException:
                if results.exists():
                    results.rename(temp/'failed')
                backup.rename(results)
                raise
        else:
            print('Figures already finalized; no replacement needed.')
    print('\n=== PUBLICATION FINALIZATION ===')
    print('Original results SHA-256:', original['evaluation_results.json'])
    print('Scientific results unchanged: PASS')
    print('Original figure set retained in Git:',archive_ref)
    print('Active figures:',len(NAMES))
    print('Obsolete active figure copies: 0')
    print('Updated manifest: PASS (7/7)')
    print('Original experiments rerun: 0')
    print('VALIDATION: PASS')

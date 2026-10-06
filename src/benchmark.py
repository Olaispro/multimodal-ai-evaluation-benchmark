"""Validate benchmark rows and summarize adjudicated outcomes."""
import argparse,json,collections
MODES={'image','audio','video'}
def summarize(rows):
 invalid=[];by=collections.defaultdict(list)
 for i,r in enumerate(rows,1):
  if r.get('modality') not in MODES or r.get('outcome') not in (0,1) or not r.get('task_id'):invalid.append(i)
  else:by[r['modality']].append(float(r['outcome']))
 summary={k:{'n':len(v),'success_rate':round(sum(v)/len(v),3)} for k,v in sorted(by.items())}
 return {'n_rows':len(rows),'invalid_rows':invalid,'by_modality':summary,'macro_success_rate':round(sum(sum(v)/len(v) for v in by.values())/len(by),3) if by else None,'scope':'Outcome labels are demo adjudications, not measured model outputs.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--out',default='benchmark-report.json');a=p.parse_args();rows=[json.loads(x) for x in open(a.input,encoding='utf-8') if x.strip()];r=summarize(rows);open(a.out,'w',encoding='utf-8').write(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
if __name__=='__main__':main()

import argparse
import re
import Pickle.my_pickle_fast as my_pickle_fast
import Json.myjson_decode as Jd
import Json.myjson_encode as Je
"""
parser = argparse.ArgumentParser(description='Json to Pickle/Pickle to Json')
parser.add_argument('indir', type=str, help='Input dir')
parser.add_argument('outdir', type=str, help='Output dir')
args = parser.parse_args()
if re.search(r'.?\.json', args.indir) is None:
    my_pickle_fast.dump(Jd.load(args.indir), args.outdir)
elif re.search(r'.?\.pickle', args.indir) is None:
    Je.dump(my_pickle_fast.load(args.indir), args.outdir)
print(args.indir, args.outdir)


indir = "test1.pickle"
outdir = "test3.json"

indir = "test.json"
outdir = "test1.pickle"
"""
indir = "test.json"
outdir = "test1.pickle"

if not re.search(r'.?\.json', indir) is None:
    with open(outdir, 'wb') as pickle_file:
        my_pickle_fast.dump(Jd.load(indir), pickle_file)
elif not re.search(r'.?\.pickle', indir) is None:
    with open(indir, 'rb') as pickle_file:
        Je.dump(my_pickle_fast.load(pickle_file), outdir)
print(indir, outdir)

indir = "test1.pickle"
outdir = "test3.json"
if not re.search(r'.?\.json', indir) is None:
    with open(outdir, 'wb') as pickle_file:
        my_pickle_fast.dump(Jd.load(indir), pickle_file)
elif not re.search(r'.?\.pickle', indir) is None:
    with open(indir, 'rb') as pickle_file:
        Je.dump(my_pickle_fast.load(pickle_file), outdir)
print(indir, outdir)

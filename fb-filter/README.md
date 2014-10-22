# fb-filter

Script to compare a year to its relevant Facebook freshers' group, and output the names of those missing from one or the other.

---

## Setup

Run the pip install in both this directory and the directory for the teachdb module. You have to do this because pip is a bit rubbish.

```
pip install -r requirements.txt
```

---

## To use:

```
$ python fb-filter.py [ic login] [fb group id] [year number]
```

So for the first year group I would do:

```
python fb-filter.py jra12 1446504498924366 1
```

You will require your Imperial password to be in the environment variable *IC_PASS*, and your Facebook access token in *FB_ACCESS*. I usually use the [graph explorer](https://developers.facebook.com/tools/explorer) to get the access token.

I recommend piping the output to a file, I've set the encoding so this won't break. Hopefully.

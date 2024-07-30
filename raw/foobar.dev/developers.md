# FooBar.DEV: Developer Documentation

This page contains the developer documentation for FooBar.DEV.
This page is also the first subpage on the Markweb! (The first *page* on the Markweb is the **FooBar.DEV** page.)

## Getting Started

To make your own page(s) on the Markweb, first clone the Ivo Markweb Server repository from GitHub [here](https://github.com/FormunaGit/ivo-markweb-serverhttps:/), and create a new folder in the `raw` directory with 2 files, `metadata.json` and a markdown file (should be called `page.md` or `index.md`.)

After you're done, just send me a pull request, let me review it, and if it's okay I will put it on the server!

### Getting a TLD

> Note: TLD = Top Level Domain (.com, .net, etc...)

Unfortunately, there is a finite amount of TLDs I can make. As much as I would want to let anyone make their own TLD, doing that would make remembering what TLD you used a lot harder and impersonation would be easier. Instead, there are currently 6 TLDs you can use in the Markweb:

* .dev
* .mw
* .wow
* .new
* .ai
* .us

If you want to register a domain with one of the above TLDs, just name your folder `yourpagesname.tld` but replace `tld` with whatever TLD you chose, and set the `tld` entry in the metadata to what you chose.

### Making the `metadata.json` file

The metadata file is what contains important information about the site, having information such as:

* The author/site developer
* A description of the site
* The filename of the landing page
* And some search engine related things.

> All websites **MUST** have the 7 JSON entries.
> JSONC (JSON with Comments) is NOT supported.

The easiest way to make a metadata file is by making a metadata file (`metadata.json`) and pasting this template:

```json
{
    "name": "Replace this with your page's title", 
    "desc": "Replace this with a description of your page",
    "tld": "Refer to ''Getting a TLD'' for what to replace this with", 
    "tags": ["replace", "this", "with", "actual", "tags"], 
    "isPublic": "true or false", 
    "author": "Replace this with your name", 
    "landPage": "Replace this with what your landing pagename is" 
}
```

> Note: the `isPublic` entry **must** be a boolean. Choose `true` if you want your page to be public, chose `false` if you want to hide it from agreeing search engines.

### Making the page

The pagename should be the same as what you wrote for the metadata `landPage` entry. If you get it wrong, your page won't be displayed, instead browsers will recieve a 404 error.

Making the actual page is very easy; just write some Markdown. You can even just write normally without any formatting, and it will turn out fine.

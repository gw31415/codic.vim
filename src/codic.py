import vim
import urllib.request
import json


def translate(token, text, project_id, casing, acronym_style):
    query = {'text': text, 'project_id': project_id,
             'casing': casing, 'acronym_style': acronym_style}
    url = "https://api.codic.jp/v1/engine/translate.json?" + \
        urllib.parse.urlencode(query)
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Bearer " + token)
    try:
        res = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    except urllib.error.URLError as e:
        return '', e
    return res[0]['translated_text'], None


out, err = translate(vim.eval('g:codic_token'), vim.eval('a:text'), vim.eval(
    'g:codic_project_id'), vim.eval('g:codic_casing'), vim.eval('g:codic_acronym_style'))
if err:
    vim.command(':echoerr "{0}"'.format(err.reason))
else:
    vim.command(':let l:out = "{0}"'.format(out))

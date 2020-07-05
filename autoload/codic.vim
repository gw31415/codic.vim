let s:scriptDir = expand('<sfile>:p:h') . '/../src/codic.py'
function! codic#translate(text)
  let l:out = ''
  execute "py3file " . s:scriptDir
  return l:out
endfunction
function! codic#dialog()
  let l:txt = input("Codic: ")
  return codic#translate(l:txt)
endfunction

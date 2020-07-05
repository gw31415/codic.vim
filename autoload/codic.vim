function! codic#translate(text)
  let l:out = ''
  py3file <sfile>:h:h/src/codic.py
  return l:out
endfunction
function! codic#dialog()
  let l:txt = input("Codic: ")
  return codic#translate(l:txt)
endfunction

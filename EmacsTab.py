import sublime, sublime_plugin

class EmacsTab(sublime_plugin.TextCommand):
  """ Provide emacs-like tab behavior """

  def run(self, edit):
    sublime.active_window().run_command('reindent')
    point = self.view.sel()[0].a
    row, col = self.view.rowcol(point)
    start_of_line = False

    # check if we are at the start of the line
    if (col == 0):
      start_of_line = True
    else:
      cur = point
      while (self.view.substr(cur - 1) == ' '):
        if self.view.rowcol(cur)[1] == 1 or cur == 0:
          start_of_line = True
          break
        cur -= 1

    if not start_of_line:
      return

    end_of_line = False
    cur = point
    while (self.view.substr(cur) == ' '):
      if self.view.rowcol(cur)[0] != row:
        end_of_line = True
        break
      cur += 1

    if not end_of_line:
      self.view.sel().clear()
      self.view.sel().add(sublime.Region(cur))
      self.view.show(cur)

import a_start_to_fit_data as fit

def main():
    files = fm.getFiles('\\AFS\ipp\home\m\mguitart\HIWI\fittings\11-30-2017')
    template = os.path.normpath('template.xnra')
    for f in files:
        fit.doFit(template, f)

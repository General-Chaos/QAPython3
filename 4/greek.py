

greek = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta',
         'Iota', 'Kappa', 'Lamda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho',
         'Final Sigma', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi',
         'Omega']

for pos, cname in enumerate(greek, start=0x03B1):
    try:
        char = chr(pos)
        upperchar = char.upper()
        print(f"{pos:#x} {cname:12s} :{char} {upperchar}")
    except UnicodeEncodeError as err:
        print(cname, 'unknown')

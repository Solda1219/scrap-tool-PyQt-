block_cipher = None
a = Analysis(['main.py'],
      pathex=['C:\\Python35\\Scripts'],
      binaries=[],
      datas=[('imports/*','data')],
      hiddenimports=[],
      hookspath=[],
      runtime_hooks=[],
      excludes=[],
      win_no_prefer_redirects=False,
      win_private_assemblies=False,
      cipher=block_cipher)

pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(pyz,
      a.scripts,
      a.binaries,
      #a.zipfiles,
      a.datas,
      name='WI-FROM Studio Ballarini.exe',
      console=False,
      windowed=True,
      debug=False,
      strip=False,
      upx=True,
      icon='logo.ico'
      )
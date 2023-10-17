# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['b64.py'],
    pathex=['./venv/lib/python3.11/site-packages'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='b64',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='b64.app',
    icon='b64.icns',
    bundle_identifier='eu.troeger.b64',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'My File Format',
                'CFBundleTypeIconFile': 'MyFileIcon.icns',
                'LSItemContentTypes': ['com.example.myformat'],
                'LSHandlerRank': 'Owner'
            }
        ]
    },
)


from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('win10toast_click')
# datas, binaries, hiddenimports += collect_all('ToastNotifier')
# datas, binaries, hiddenimports += collect_all('win10toast')

import { app, BrowserWindow } from 'electron'
import path from 'path'
/**
 * Set `__static` path to static files in production
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html
 */
if (process.env.NODE_ENV !== 'development') {
  global.__static = require('path').join(__dirname, '/static').replace(/\\/g, '\\\\')
}

let mainWindow
const winURL = process.env.NODE_ENV === 'development'
  ? `http://localhost:9080`
  : `file://${__dirname}/index.html`

function createWindow () {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    height: 563,
    useContentSize: true,
    width: 1000
  })

  mainWindow.loadURL(winURL)

  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})

/**
 * Auto Updater
 *
 * Uncomment the following code below and install `electron-updater` to
 * support auto updating. Code Signing with a valid certificate is required.
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-electron-builder.html#auto-updating
 */

/*
import { autoUpdater } from 'electron-updater'

autoUpdater.on('update-downloaded', () => {
  autoUpdater.quitAndInstall()
})

app.on('ready', () => {
  if (process.env.NODE_ENV === 'production') autoUpdater.checkForUpdates()
})
 */

// add these to the end or middle of main.js

let pyProc = null
let pyPort = null

const selectPort = () => {
  pyPort = 4242
  return pyPort
}

const createPyProc = () => {
  // let port = '' + selectPort()
  let script = path.join(__dirname, '../../app.py')
  pyProc = require('child_process').spawn('/Library/Frameworks/Python.framework/Versions/3.8/bin/python3', [script,])
  pyProc.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  pyProc.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  
  
  if (pyProc != null) {
    console.log('child process success- flask server created')
  } else {
    console.log('ERROR: failed to start flask server')
  }
}

const exitPyProc = () => {
  pyProc.kill()
  pyProc = null
  pyPort = null
}

app.on('ready', createPyProc)
app.on('will-quit', exitPyProc)
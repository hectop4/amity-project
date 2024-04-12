const { app, BrowserWindow } = require("electron/main");
const path = require("node:path");
const express = require("express");

function createWindow() {
  const win = new BrowserWindow({
    titleBarStyle: "hidden",
    titleBarOverlay: {
      color: "#2f3241",
      symbolColor: "#74b1be",
      height: 60,
    },
    width: 800,
    height: 600,
  });

  win.loadURL("http://127.0.0.1:3000");
}

app.whenReady().then(() => {
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

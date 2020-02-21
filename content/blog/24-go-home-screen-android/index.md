---
title: "Go Home Screen Android"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: ""
---
# Go Home Screen Android

```
    Intent startMain = new Intent(Intent.ACTION_MAIN);
    startMain.addCategory(Intent.CATEGORY_HOME);
    startMain.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    startActivity(startMain);

```


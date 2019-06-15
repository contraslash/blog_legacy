Title: Go Home Screen Android
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: 
---
# Go Home Screen Android

```
	Intent startMain = new Intent(Intent.ACTION_MAIN);
    startMain.addCategory(Intent.CATEGORY_HOME);
    startMain.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    startActivity(startMain);

```
---
title: "Compartir en redes sociales con un vínculo"
date: "2016-04-15T01:23:52+00:00"
description: ""
tags: "Web Apps,Social Media"
---
# Compartir en redes sociales con un vínculo

Esta respuesta fue tomada de  [Aquí](http://stackoverflow.com/questions/9120539/facebook-share-link-no-javascript)

Y dice

**Facebook**
```
<a href="https://www.facebook.com/sharer/sharer.php?u=URLENCODED_URL&t=TITLE"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600');return false;"
   target="_blank" title="Share on Facebook">
</a>
```

**Twitter**
```
<a href="https://twitter.com/share?url=URLENCODED_URL&via=TWITTER_HANDLE&text=TEXT"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600');return false;"
   target="_blank" title="Share on Twitter">
</a>
```

**Google Plus**
```
<a href="https://plus.google.com/share?url=URLENCODED_URL"
   onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=350,width=480');return false;"
   target="_blank" title="Share on Google+">
</a>
```




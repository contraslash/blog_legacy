Title: umano AndroidSlidingUpPanel
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Android
---
# umano AndroidSlidingUpPanelSi estas tratando de compilar un viejo proyecto que usa 
umano SlidingUpPanel para android, no olvides poner el prefijo unabi a todos los atributos en la etiqueta sothree :3

Tambien recuerda que los métodos expandPanel y hidePanel no están disponibles, así que debes usar getPanelState y setPanelState, haciendo algo como esto:


```if( slidingPanel.getPanelState() !=  SlidingUpPanelLayout.PanelState.EXPANDED)
{
	slidingPanel.setPanelState(SlidingUpPanelLayout.PanelState.EXPANDED);
}
 ```

Bueno, eso funcionó para mí



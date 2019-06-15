Title: NavigationView Android Material
Date: 2016-01-29T06:42:23+00:00
Description: Implementación de un NavigationView en Android usando las librerías de compatiblidad para Material Design de Google
Tags: Android,Material Design,Enlaces útiles
---
# NavigationView Android Material

Definitivamente tener una lista de enlaces útiles  que saquen de apuros es algo maravilloso, y [este artículo](http://blog.xebia.com/2015/06/09/android-design-support-navigationview/) definitivamente me ha sacado de apuros mas de una vez.

Para la definición del layout principal necesitaremos una estructura similar a esta

```
<android.support.v4.widget.DrawerLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/main_drawer_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true">

   <!-- Main Content Here! -->
<android.support.design.widget.NavigationView
        android:id="@+id/navigation"
        android:layout_width="wrap_content"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        android:background="@color/white"
        app:itemIconTint="@color/primary"
        app:itemTextColor="@color/primary_dark"
        app:menu="@menu/drawer"

        />
</android.support.v4.widget.DrawerLayout>
```

app:menu nos refiere a un archivo que debemos colocar en la carpeta menus de res

```
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <group android:checkableBehavior="single">

        <item
            android:id="@+id/menu_drawer_it1"
            android:icon="@drawable/drawable1"
            android:title="@string/some_string"/>

        <!-- Other items here -->

    </group>
</menu>
```


En la actividad que contiene el navigationview necesitaremos algo parecido a esto

```
// Imports over here

public class MainActivity extends AppCompatActivity implements
        NavigationView.OnNavigationItemSelectedListener
{
    DrawerLayout mDrawerLayout;
    private ActionBarDrawerToggle mDrawerToggle;
    private final Handler mDrawerActionHandler = new Handler();
    private int mNavItemId;

    private static final String NAV_ITEM_ID = "nav_item_id";
    private static final long DRAWER_CLOSE_DELAY_MS = 250;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Other things in here
        if (null == savedInstanceState) {
            mNavItemId = R.id.menu_drawer_it1;
        } else {
            mNavItemId = savedInstanceState.getInt(NAV_ITEM_ID);
        }
        
        mDrawerLayout = (DrawerLayout) findViewById(R.id.main_drawer_layout);

        NavigationView navigationView = (NavigationView) findViewById(R.id.navigation);
        LayoutInflater inflater=(LayoutInflater)getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        navigationView.setNavigationItemSelectedListener(this);

        // select the correct nav menu item
        MenuItem menuItem = navigationView.getMenu().findItem(mNavItemId);
        if(menuItem!=null)
        {
            menuItem.setChecked(true);
        }


        // set up the hamburger icon to open and close the drawer
        mDrawerToggle = new ActionBarDrawerToggle(
                this,
                mDrawerLayout,
                mToolbar,
                R.string.open,
                R.string.close
        );
        mDrawerLayout.setDrawerListener(mDrawerToggle);
        mDrawerToggle.syncState();

        navigate(mNavItemId);

        // More things over here

    }

    @Override
    public boolean onNavigationItemSelected(final MenuItem menuItem) {
        // update highlighted item in the navigation menu
        menuItem.setChecked(true);
        mNavItemId = menuItem.getItemId();

        // allow some time after closing the drawer before performing real navigation
        // so the user can see what is happening
        mDrawerLayout.closeDrawer(GravityCompat.START);
        mDrawerActionHandler.postDelayed(new Runnable() {
            @Override
            public void run() {
                navigate(menuItem.getItemId());
            }
        }, DRAWER_CLOSE_DELAY_MS);
        return true;
    }
    private void navigate(final int itemId) {
        // perform the actual navigation logic, updating the main content fragment etc
        switch (itemId) {

        }
    }

    @Override
    public void onConfigurationChanged(final Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        mDrawerToggle.onConfigurationChanged(newConfig);
    }
    @Override
    protected void onSaveInstanceState(final Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putInt(NAV_ITEM_ID, mNavItemId);
    }

    @Override
    public void onBackPressed() {
        if (mDrawerLayout.isDrawerOpen(GravityCompat.START)) {
            mDrawerLayout.closeDrawer(GravityCompat.START);
        } else if(mDrawerLayout.isDrawerOpen(GravityCompat.END)){
            mDrawerLayout.closeDrawer(GravityCompat.END);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onPostCreate(Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);
        // Sync the toggle state after onRestoreInstanceState has occurred.
        mDrawerToggle.syncState();
```

También necesitamos añadir algunos strings en res

``` 
    <string name="open">Abrir</string>
    <string name="close">Cerrar</string>
```

> ATENCIÓN: Los snippets anteriores son solo una plantilla, deben ajustarse a la necesidad específica de cada proyecto
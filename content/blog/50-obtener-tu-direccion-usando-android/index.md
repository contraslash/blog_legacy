---
title: "Obtener tu dirección usando Android"
date: "2016-01-29T06:42:23+00:00"
description: ""
tags: "Android,GPS,Direccion"
---
# Obtener tu dirección usando Android

```
/**
     * Clase que usa el GeoCoder para obtener la dirección actual
     */
    private class GetDireccion extends AsyncTask<LatLng, Void, String> {
        Context mContext;
        String idedit;
        public GetDireccion(Context context, String id) {
            super();
            Log.i(TAG,"Creando el AsyncTask GetDireccion");
            mContext = context;
            idedit=id;
        }

        /**
         * Gestor de obtención dedirección
         */
        @Override
        protected String doInBackground(LatLng... params) {
            Geocoder geocoder =
                    new Geocoder(mContext, Locale.getDefault());
            if(params[0]==null)
                return "";
            LatLng loc = params[0];
            List<Address> addresses = null;
            try {
                /*
                 * Return 1 address.
                 */
                Log.i(TAG,"Intentando obtener la dirección del punto: "+loc.latitude+","+loc.longitude);
                addresses = geocoder.getFromLocation(loc.latitude,
                        loc.longitude, 1);
            } catch (IOException e1) {
                Log.e(TAG,
                        "IO Exception in getFromLocation()");
                //Toast.makeText(getActivity(),"Imposible obtener su ubicación, verifique el GPS esté activado",Toast.LENGTH_LONG).show();
                e1.printStackTrace();
                return "";
            } catch (IllegalArgumentException e2)
            {
                String errorString = "Illegal arguments " +
                        Double.toString(loc.latitude) +
                        " , " +
                        Double.toString(loc.longitude) +
                        " passed to address service";
                Log.e(TAG, errorString);
                e2.printStackTrace();
                return "";
            }
            if (addresses != null && addresses.size() > 0) {
                Address address = addresses.get(0);
                String addressText = address.getMaxAddressLineIndex() > 0 ?
                                address.getAddressLine(0) : "";
                StringTokenizer st=new StringTokenizer(addressText);
                String simplifyDir="";
                while(st.hasMoreTokens())
                {
                    String a=st.nextToken();
                    if(a.compareTo("a")==0)
                    {
                        break;
                    }
                    else
                    {
                        simplifyDir+=a+" ";
                    }
                }
                return simplifyDir;
            } else {
                return "No encontramos la direccion";
            }
        }

        /**
         * Método para mostrar la dirección en la interfaz gráfica
         */
        @Override
        protected void onPostExecute(String address) {

        }
    }
```


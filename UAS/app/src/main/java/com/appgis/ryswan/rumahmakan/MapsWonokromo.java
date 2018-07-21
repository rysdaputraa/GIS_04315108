package com.appgis.ryswan.rumahmakan;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class MapsWonokromo extends FragmentActivity implements OnMapReadyCallback {

    protected Cursor cursor;
    private GoogleMap mMap;
    DataHelper dbHelper;
    String no, nama, alamat;
    double latitude ;
    double longi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps_wonokromo);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        dbHelper = new DataHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();
        cursor = db.rawQuery("SELECT * FROM tb_rumahmakan WHERE nama = '" +
                getIntent().getStringExtra("nama") + "'",null);
        cursor.moveToFirst();
        if (cursor.getCount()>0)
        {
            cursor.moveToPosition(0);
            no = (cursor.getString(0).toString());
            nama =(cursor.getString(1).toString());
            latitude = (cursor.getDouble(2));
            longi = (cursor.getDouble(3));
            alamat = (cursor.getString(4).toString());

        }
    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        // Add a marker in Sydney and move the camera

        mMap = googleMap;
        mMap.setMapType(googleMap.MAP_TYPE_NORMAL);
        LatLng p = new LatLng(latitude, longi);
        mMap.addMarker(new MarkerOptions().position(p).title(nama));
        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(p, 17f));
    }
}

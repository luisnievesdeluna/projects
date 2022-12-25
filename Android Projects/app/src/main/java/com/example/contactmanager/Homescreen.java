package com.example.contactmanager;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class Homescreen extends AppCompatActivity {

    Button logoffButton;
    Button profileButton;
    Button contactButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_homescreen);

        logoffButton = findViewById(R.id.lo_button);
        profileButton = findViewById(R.id.pf_button);
        contactButton = findViewById(R.id.ct_button);

        logoffButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Logout();
            }
        });

        profileButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Profile();
            }
        });

        contactButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Contacts();
            }
        });
    }
    public void Logout()
    {
        Intent intent = new Intent(this, Login.class);
        startActivity(intent);
    }

    public void Profile()
    {
        Intent intent = new Intent(this, Profile.class);
        startActivity(intent);
    }

    public void Contacts()
    {
        Intent intent = new Intent(this, Contacts.class);
        startActivity(intent);
    }
}
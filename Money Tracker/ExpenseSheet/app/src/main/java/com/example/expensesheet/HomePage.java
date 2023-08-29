package com.example.expensesheet;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class HomePage extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);



        Intent intent = getIntent();
        String username = intent.getStringExtra("username");

        TextView textView = findViewById(R.id.textView);

        textView.setText("Welcome back " + username + ", Please select action");

        Button logExpense = findViewById(R.id.log_button);
        logExpense.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(HomePage.this, LogExpense.class);
                intent.putExtra("username", username);
                startActivity(intent);
            }
        });

        Button viewExpenses = findViewById(R.id.view_button);
        viewExpenses.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(HomePage.this, ViewExpenses.class);
                intent.putExtra("username", username);
                startActivity(intent);
            }
        });

        Button viewProfile = findViewById(R.id.user_button);
        viewProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(HomePage.this, UserProfile.class);
                intent.putExtra("username", username);
                startActivity(intent);
            }
        });

    }
}
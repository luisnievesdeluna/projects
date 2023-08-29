package com.example.expensesheet;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QuerySnapshot;

public class CreateProfile extends AppCompatActivity {

    EditText username;
    EditText password;
    EditText fname;
    EditText lname;
    EditText email;

    FirebaseFirestore db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_profile);
        username = (EditText) findViewById(R.id.username);
        password = (EditText) findViewById(R.id.create_password);
        fname = (EditText) findViewById(R.id.create_firstname);
        lname = (EditText) findViewById(R.id.create_lastname);
        email = (EditText) findViewById(R.id.create_email);

        db = FirebaseFirestore.getInstance();
    }

    public void save(View v)
    {
        String usernameValue = username.getText().toString();
        String passwordValue = password.getText().toString();
        String fnameValue = fname.getText().toString();
        String lnameValue = lname.getText().toString();
        String emailValue = email.getText().toString();

        String regexPattern = "^[a-zA-Z0-9_]+$";

        if (usernameValue.isEmpty() || passwordValue.isEmpty() || fnameValue.isEmpty() || lnameValue.isEmpty() || emailValue.isEmpty()) {
            Toast.makeText(getApplicationContext(), "Please fill out all the details!", Toast.LENGTH_SHORT).show();
        }



        if (!usernameValue.matches(regexPattern))
        {
            Toast.makeText(getApplicationContext(), "Special character(s) detected. Not allowed. ", Toast.LENGTH_SHORT).show();
        }
        else {
            // Check if user with the given username already exists
            Query query = db.collection("users").whereEqualTo("username", usernameValue);
            query.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                @Override
                public void onComplete(@NonNull Task<QuerySnapshot> task) {
                    if (task.isSuccessful()) {
                        QuerySnapshot querySnapshot = task.getResult();
                        if (querySnapshot.isEmpty()) {
                            // User does not exist, proceed with creating the user
                            DBCreate dbCreate = new DBCreate(username.getText().toString(), password.getText().toString(), fname.getText().toString(), lname.getText().toString(), email.getText().toString());
                            db.collection("users")
                                    .document(username.getText().toString())
                                    .set(dbCreate)
                                    .addOnCompleteListener(new OnCompleteListener<Void>() {
                                        @Override
                                        public void onComplete(@NonNull Task<Void> task) {
                                            if (task.isSuccessful()) {
                                                Toast.makeText(getApplicationContext(), "User is now created!", Toast.LENGTH_LONG).show();
                                                Intent intent = new Intent(CreateProfile.this, MainActivity.class);
                                                startActivity(intent);
                                            }

                                        }
                                    });
                        } else {
                            // User already exists
                            Toast.makeText(getApplicationContext(), "User already exists!", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        // An error occurred while querying the Firestore collection
                        Toast.makeText(getApplicationContext(), "Error occurred while checking user existence", Toast.LENGTH_SHORT).show();
                    }
                }
            });
        }
    }
}
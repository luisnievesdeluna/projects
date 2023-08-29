package com.example.expensesheet;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QuerySnapshot;

public class MainActivity extends AppCompatActivity {

    EditText username;
    EditText password;

    FirebaseFirestore db;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username = (EditText) findViewById(R.id.username);
        password = (EditText) findViewById(R.id.password);

        db = FirebaseFirestore.getInstance();

        Button Create = findViewById(R.id.create);
        Create.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Intent to navigate to the next activity
                Intent intent = new Intent(MainActivity.this, CreateProfile.class);
                startActivity(intent);
            }
        });
        Button Signin = findViewById(R.id.signin);
        Signin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String usernameValue = username.getText().toString();
                String passwordValue = password.getText().toString();
                if (usernameValue.isEmpty() || passwordValue.isEmpty()) {
                    Toast.makeText(getApplicationContext(), "Please fill out all the details!", Toast.LENGTH_SHORT).show();

                }
                else
                {
                    Query query = db.collection("users")
                            .whereEqualTo("username", usernameValue);
                            //.whereEqualTo("password", passwordValue);
                    query.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                        @Override
                        public void onComplete(@NonNull Task<QuerySnapshot> task) {
                            if (task.isSuccessful())
                            {
                                QuerySnapshot querySnapshot = task.getResult();
                                if (querySnapshot.isEmpty())
                                {
                                    Toast.makeText(getApplicationContext(), "User does not exist! Please register", Toast.LENGTH_SHORT).show();
                                }
                                else
                                {
                                    Query secondQuery = db.collection("users")
                                                    .whereEqualTo("username", usernameValue).whereEqualTo("password", passwordValue);
                                    secondQuery.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                                        @Override
                                        public void onComplete(@NonNull Task<QuerySnapshot> secondTask) {
                                            if (secondTask.isSuccessful())
                                            {
                                                QuerySnapshot secondQuerySnapshot = secondTask.getResult();
                                                if (secondQuerySnapshot.isEmpty())
                                                {
                                                    Toast.makeText(getApplicationContext(), "Invalid username/password. Please try again!", Toast.LENGTH_SHORT).show();
                                                }
                                                else
                                                {
                                                    Toast.makeText(getApplicationContext(), "Welcome back" + " " + usernameValue, Toast.LENGTH_SHORT).show();
                                                    Intent intent = new Intent(MainActivity.this, HomePage.class);
                                                    intent.putExtra("username", usernameValue);
                                                    startActivity(intent);
                                                }
                                            }

                                        }
                                    });

                                }
                            }
                        }
                    });
                }
            }
        });

    }
}
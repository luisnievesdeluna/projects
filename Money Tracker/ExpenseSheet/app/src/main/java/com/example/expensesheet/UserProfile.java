package com.example.expensesheet;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentId;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QuerySnapshot;

public class UserProfile extends AppCompatActivity {

    FirebaseFirestore db;

    AlertDialog dialog;
    AlertDialog.Builder builder;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_profile);

        TextView jobTitle = findViewById(R.id.jobtitle);
        TextView income = findViewById(R.id.income);
        TextView typeJob = findViewById(R.id.fptype);


        Intent intent = getIntent();
        String username = intent.getStringExtra("username");

        db = FirebaseFirestore.getInstance();

        builder = new AlertDialog.Builder(UserProfile.this);
        builder.setTitle("Please confirm or cancel").setMessage("You currently don't have any job information down, will you like to input?");

        Button updateProfile = findViewById(R.id.updatepro);
        updateProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(UserProfile.this, UpdateProfile.class);
                intent.putExtra("username", username);
                startActivity(intent);
            }
        });

        CollectionReference incomeColRef = db.collection("users")
                .document(username)
                .collection("income source");

        incomeColRef.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if (task.isSuccessful())
                {
                    if(task.getResult().isEmpty())
                    {
                        builder.setPositiveButton(
                                "Yes",
                                new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialogInterface, int i) {
                                        Intent intent = new Intent(UserProfile.this, UpdateProfile.class);
                                        intent.putExtra("username", username);
                                        startActivity(intent);

                                    }
                                }
                        );

                        builder.setNegativeButton(
                                "No",
                                new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialogInterface, int i) {
                                        Toast.makeText(getApplicationContext(), "Action Cancelled!", Toast.LENGTH_SHORT).show();
                                        finish();
                                    }
                                });
                        AlertDialog alert1 = builder.create();
                        alert1.show();
                    }
                    else
                    {
                        DocumentReference infoDocRef = db.collection("users")
                                .document(username)
                                .collection("income source")
                                .document("job info");

                        infoDocRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                            @Override
                            public void onComplete(@NonNull Task<DocumentSnapshot> task) {
                                if(task.isSuccessful())
                                {
                                    DocumentSnapshot documentSnapshot = task.getResult();
                                    if(documentSnapshot.exists())
                                    {
                                        String jobData = documentSnapshot.getString("jobtitle");
                                        String salaryData = documentSnapshot.getString("salary");
                                        String typeData = documentSnapshot.getString("type");


                                        jobTitle.setText(jobData);
                                        income.setText(salaryData);
                                        typeJob.setText(typeData);

                                    }
                                }
                            }
                        });

                    }
                }
                else
                {
                    Toast.makeText(getApplicationContext(), "There was an error connecting to database, please try again later!", Toast.LENGTH_SHORT).show();
                }
            }
        });




    }
}
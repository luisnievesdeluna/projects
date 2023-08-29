package com.example.expensesheet;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.tabs.TabLayout;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QuerySnapshot;

import java.lang.invoke.ConstantCallSite;
import java.util.Map;

public class UpdateProfile extends AppCompatActivity {

    EditText jobTitle;
    EditText salary;
    EditText type;

    FirebaseFirestore db;

    AlertDialog dialog;
    AlertDialog.Builder builder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_update_profile);

        jobTitle = (EditText) findViewById(R.id.job_title);
        salary = (EditText) findViewById(R.id.salary);
        type = (EditText) findViewById(R.id.type);

        db = FirebaseFirestore.getInstance();

        builder = new AlertDialog.Builder(UpdateProfile.this);
        builder.setTitle("Please confirm or cancel").setMessage("Are you sure you want to update?");

        Intent intent = getIntent();
        String username = intent.getStringExtra("username");

        Button Updateprofile = findViewById(R.id.update_profile);

        Updateprofile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String jobValue = jobTitle.getText().toString();
                String salaryValue = salary.getText().toString();
                String typeValue = type.getText().toString();

                if(jobValue.isEmpty() || salaryValue.isEmpty())  {
                    Toast.makeText(getApplicationContext(), "Please fill out all the details!", Toast.LENGTH_SHORT).show();
                }

                else
                {
                    CollectionReference incomeColRef = db.collection("users")
                                                    .document(username)
                                                    .collection("income source");

                    incomeColRef.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                        @Override
                        public void onComplete(@NonNull Task<QuerySnapshot> task) {
                            if (task.isSuccessful())
                            {
                                if (!task.getResult().isEmpty())
                                {
                                    builder.setPositiveButton(
                                            "Yes",
                                            new DialogInterface.OnClickListener() {
                                                @Override
                                                public void onClick(DialogInterface dialogInterface, int i) {
                                                    DBJobInfo dbJobInfo = new DBJobInfo(jobValue, salaryValue, typeValue);
                                                    db.collection("users")
                                                            .document(username)
                                                            .collection("income source")
                                                            .document("job info")
                                                            .set(dbJobInfo)
                                                            .addOnCompleteListener(new OnCompleteListener<Void>() {
                                                                @Override
                                                                public void onComplete(@NonNull Task<Void> secondTask) {
                                                                    if (secondTask.isSuccessful())
                                                                    {
                                                                        Toast.makeText(getApplicationContext(), "Job info recorded!", Toast.LENGTH_SHORT).show();
                                                                        Intent intent = new Intent(UpdateProfile.this, UserProfile.class);
                                                                        intent.putExtra("username", username);
                                                                        startActivity(intent);
                                                                    }

                                                                }
                                                            });
                                                }
                                            });

                                    builder.setNegativeButton(
                                            "No",
                                            new DialogInterface.OnClickListener() {
                                                @Override
                                                public void onClick(DialogInterface dialogInterface, int i) {
                                                    Toast.makeText(getApplicationContext(), "Action cancelled!", Toast.LENGTH_SHORT).show();

                                                }
                                            });
                                    AlertDialog alertDialog = builder.create();
                                    alertDialog.show();


                                }
                                else
                                {
                                   DBJobInfo dbJobInfo = new DBJobInfo(jobValue, salaryValue, typeValue);
                                   db.collection("users")
                                           .document(username)
                                           .collection("income source")
                                           .document("job info")
                                           .set(dbJobInfo)
                                           .addOnCompleteListener(new OnCompleteListener<Void>() {
                                               @Override
                                               public void onComplete(@NonNull Task<Void> secondTask) {
                                                   if (secondTask.isSuccessful())
                                                   {
                                                       Toast.makeText(getApplicationContext(), "Job info recorded!", Toast.LENGTH_SHORT).show();
                                                       Intent intent = new Intent(UpdateProfile.this, UserProfile.class);
                                                       intent.putExtra("username", username);
                                                       startActivity(intent);
                                                   }
                                               }
                                           });
                                }
                            }
                            else
                            {
                                Toast.makeText(getApplicationContext(), "Error checking the database for your job information, please try again later!", Toast.LENGTH_SHORT).show();
                            }
                        }
                    });


                }
            }
        });
    }
}
package com.example.expensesheet;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.List;

public class ViewExpenses extends AppCompatActivity {

    FirebaseFirestore db;

    AlertDialog dialog;
    AlertDialog.Builder builder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_expenses);

        Spinner weekSpinner = findViewById(R.id.weekSpinner);
        Spinner expSpinner = findViewById(R.id.expSpinner);

        TextView dayValueView = findViewById(R.id.tempDay);
        TextView categoryValueView = findViewById(R.id.categoryDescrip);
        TextView amountValueView = findViewById(R.id.amountSpent);
        TextView budgetValueView = findViewById(R.id.amountBudg);

        Intent intent = getIntent();
        String username = intent.getStringExtra("username");

        db = FirebaseFirestore.getInstance();

        builder = new AlertDialog.Builder(ViewExpenses.this);
        builder.setTitle("Please confirm or cancel").setMessage("You currently don't have any expenses, would you like to log your first one?");

        CollectionReference weekColRef = db.collection("users")
                .document(username)
                .collection("weeklyExpenses");

        weekColRef.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
            if (task.isSuccessful())
            {
                List<String> weekNum = new ArrayList<>();

                for (QueryDocumentSnapshot document : task.getResult()) {
                    String weekValue = document.getId();
                    weekNum.add(weekValue);
                }

                ArrayAdapter<String> adapter = new ArrayAdapter<>(ViewExpenses.this, android.R.layout.simple_spinner_item, weekNum);
                adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                weekSpinner.setAdapter(adapter);

            }
            else
            {
                builder.setPositiveButton(
                        "Yes",
                        new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                Intent intent = new Intent(ViewExpenses.this, LogExpense.class);
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
                        }
                );
                AlertDialog alert1 = builder.create();
                alert1.show();
            }
            }
        });

        weekSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int position, long id) {

                String weekSelected = (String) adapterView.getItemAtPosition(position);

                CollectionReference expColRef = db.collection("users")
                        .document(username)
                        .collection("weeklyExpenses")
                        .document(weekSelected)
                        .collection("expenses");

                expColRef.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<QuerySnapshot> secondTask) {
                        if (secondTask.isSuccessful())
                        {
                            List<String> expNum = new ArrayList<>();

                            for(QueryDocumentSnapshot secondDocument : secondTask.getResult())
                            {
                                String expValue = secondDocument.getId();
                                expNum.add(expValue);
                            }

                            ArrayAdapter<String> secondAdapter = new ArrayAdapter<>(ViewExpenses.this, android.R.layout.simple_spinner_item, expNum);
                            secondAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                            expSpinner.setAdapter(secondAdapter);
                        }
                        else
                        {
                            Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
                        }
                    }
                });

                expSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
                    @Override
                    public void onItemSelected(AdapterView<?> adapterView, View view, int position, long id) {

                        String expenseSelected = (String) adapterView.getItemAtPosition(position);

                        DocumentReference expDocRef = db.collection("users")
                                .document(username)
                                .collection("weeklyExpenses")
                                .document(weekSelected)
                                .collection("expenses")
                                .document(expenseSelected);

                        expDocRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                            @Override
                            public void onComplete(@NonNull Task<DocumentSnapshot> thirdTask) {
                                 if (thirdTask.isSuccessful())
                                 {
                                     DocumentSnapshot documentSnapshot = thirdTask.getResult();

                                     if(documentSnapshot.exists())
                                     {
                                         String day = documentSnapshot.getString("day");
                                         String amountSpent = documentSnapshot.getString("amountSpent");
                                         String amountBudgeted = documentSnapshot.getString("moneyBudgeted");
                                         String category = documentSnapshot.getString("category");

                                         dayValueView.setText(day);
                                         categoryValueView.setText(category);
                                         amountValueView.setText(amountSpent);
                                         budgetValueView.setText(amountBudgeted);


                                     }
                                     else
                                     {
                                         Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
                                     }
                                 }
                                 else
                                 {
                                     Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
                                 }
                            }
                        });

                    }

                    @Override
                    public void onNothingSelected(AdapterView<?> adapterView) {
                    //expense if nothing selected

                    }
                });

            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {
            //week if nothing selected
                expSpinner.setVisibility(View.GONE);

            }
        });



    }
}
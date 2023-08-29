package com.example.expensesheet;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Dialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.HashMap;

public class LogExpense extends AppCompatActivity {

    EditText amountSpent;
    EditText category;
    EditText description;
    EditText moneyBudgeted;
    EditText expenseNumber;
    EditText weekNumber;
    EditText day;

    FirebaseFirestore db;

    AlertDialog dialog;
    AlertDialog.Builder builder;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_log_expense);

        amountSpent = (EditText) findViewById(R.id.amount_spent);
        category = (EditText) findViewById(R.id.category);
        description = (EditText) findViewById(R.id.expense_description);
        moneyBudgeted = (EditText) findViewById(R.id.budgeted_amount);
        expenseNumber = (EditText) findViewById(R.id.expense_number);
        weekNumber = (EditText) findViewById(R.id.week_number);
        day = (EditText) findViewById(R.id.day);

        db = FirebaseFirestore.getInstance();

        Intent intent = getIntent();
        String username = intent.getStringExtra("username");

        TextView textView = findViewById(R.id.text_log_expenses);
        textView.setText("Welcome back " + username + ", Please select action");

        builder = new AlertDialog.Builder(LogExpense.this);
        builder.setTitle("Please confirm or cancel").setMessage("There was an expense found with this ID. Do you want to override this expense?");


        Button recordAmount = findViewById(R.id.record_amount);
        recordAmount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String amountValue = amountSpent.getText().toString();
                String categoryValue = category.getText().toString();
                String descriptionValue = description.getText().toString();
                String budgetedValue = moneyBudgeted.getText().toString();
                String expenseNumberValue  = expenseNumber.getText().toString();
                String weekNumberValue = weekNumber.getText().toString();
                String dayValue = day.getText().toString();


                if(amountValue.isEmpty() || categoryValue.isEmpty() || descriptionValue.isEmpty() || budgetedValue.isEmpty() || expenseNumberValue.isEmpty() || weekNumberValue.isEmpty() || dayValue.isEmpty())
                {
                    Toast.makeText(getApplicationContext(), "Please fill out all the details!", Toast.LENGTH_SHORT).show();
                }

                else
                {
                    //checking to see if the user actually exists in the database
                    Query query = db.collection("users").whereEqualTo("username", username);
                    query.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                        @Override
                        public void onComplete(@NonNull Task<QuerySnapshot> task) {
                           if(task.isSuccessful())
                           {
                               QuerySnapshot querySnapshot = task.getResult();
                               if (querySnapshot.isEmpty())
                               {
                                   Toast.makeText(getApplicationContext(), "Sorry, there has been a database error. Please try again later", Toast.LENGTH_SHORT).show();
                               }
                               else
                               {
                                   //check to see if the week number already exists
                                   DocumentReference weekDocRef = db.collection("users")
                                           .document(username)
                                           .collection("weeklyExpenses")
                                           .document("week " + weekNumberValue);

                                   weekDocRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                                       @Override
                                       public void onComplete(@NonNull Task<DocumentSnapshot> task) {
                                           if (task.isSuccessful())
                                           {
                                               //check to see if the expense already exists

                                               DocumentReference expDocRef = db.collection("users")
                                                       .document(username)
                                                       .collection("weeklyExpenses")
                                                       .document("week " + weekNumberValue)
                                                       .collection("expenses")
                                                       .document("expense " + expenseNumberValue);

                                               expDocRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                                                   @Override
                                                   public void onComplete(@NonNull Task<DocumentSnapshot> secondTask) {
                                                       if(secondTask.isSuccessful())
                                                       {
                                                           DocumentSnapshot expDocSnapshot = secondTask.getResult();
                                                           if (expDocSnapshot.exists())
                                                           {
                                                           builder.setPositiveButton(
                                                                   "Yes",
                                                                   new DialogInterface.OnClickListener() {
                                                                       @Override
                                                                       public void onClick(DialogInterface dialogInterface, int i) {
                                                                           DBLogExpense dbLogExpense = new DBLogExpense
                                                                                   (amountValue,
                                                                                   categoryValue,
                                                                                   descriptionValue,
                                                                                   budgetedValue,
                                                                                   dayValue);
                                                                           db.collection("users")
                                                                                   .document(username)
                                                                                   .collection("weeklyExpenses")
                                                                                   .document("week " + weekNumberValue)
                                                                                   .collection("expenses")
                                                                                   .document("expense " + expenseNumberValue)
                                                                                   .set(dbLogExpense)
                                                                                   .addOnCompleteListener(new OnCompleteListener<Void>() {
                                                                                       @Override
                                                                                       public void onComplete(@NonNull Task<Void> thirdTask) {
                                                                                           if (thirdTask.isSuccessful())
                                                                                           {
                                                                                               Toast.makeText(getApplicationContext(), "Your expense has been logged!", Toast.LENGTH_SHORT).show();
                                                                                           }
                                                                                           else
                                                                                           {
                                                                                               Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
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
                                                                           Toast.makeText(getApplicationContext(), "Action Cancelled!", Toast.LENGTH_SHORT).show();
                                                                       }
                                                                   });
                                                           AlertDialog alertDialog = builder.create();
                                                           alertDialog.show();
                                                           }
                                                           else
                                                           {
                                                               //Checking to see if the document exists to create it or not
                                                              DocumentReference weekDocRef = db.collection("users")
                                                                      .document(username)
                                                                      .collection("weeklyExpenses")
                                                                      .document("week " + weekNumberValue);

                                                              weekDocRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                                                                  @Override
                                                                  public void onComplete(@NonNull Task<DocumentSnapshot> task) {
                                                                  if (task.isSuccessful())
                                                                  {
                                                                      DocumentSnapshot weekSnapshot= task.getResult();
                                                                      if (weekSnapshot.exists())
                                                                      {
                                                                          //create expense with week number already existing
                                                                          DBLogExpense dbLogExpense = new DBLogExpense
                                                                                  (amountValue,
                                                                                          categoryValue,
                                                                                          descriptionValue,
                                                                                          budgetedValue,
                                                                                          dayValue);
                                                                          db.collection("users")
                                                                                  .document(username)
                                                                                  .collection("weeklyExpenses")
                                                                                  .document("week " + weekNumberValue)
                                                                                  .collection("expenses")
                                                                                  .document("expense " + expenseNumberValue)
                                                                                  .set(dbLogExpense)
                                                                                  .addOnCompleteListener(new OnCompleteListener<Void>() {
                                                                                      @Override
                                                                                      public void onComplete(@NonNull Task<Void> task) {
                                                                                          if (task.isSuccessful())
                                                                                          {
                                                                                              Toast.makeText(getApplicationContext(), "Your expense has been logged", Toast.LENGTH_SHORT).show();
                                                                                          }
                                                                                      }
                                                                                  });
                                                                      }
                                                                      else
                                                                      {
                                                                      //create the week first then expense
                                                                      DocumentReference weekCreationRef = db.collection("users")
                                                                              .document(username)
                                                                              .collection("weeklyExpenses")
                                                                              .document("week " + weekNumberValue);

                                                                      weekCreationRef.set(new HashMap<>()) // You can pass an empty map or no data
                                                                              .addOnSuccessListener(new OnSuccessListener<Void>() {
                                                                                  @Override
                                                                                  public void onSuccess(Void aVoid) {
                                                                                      //create expense
                                                                                      DBLogExpense dbLogExpense = new DBLogExpense
                                                                                              (amountValue,
                                                                                                      categoryValue,
                                                                                                      descriptionValue,
                                                                                                      budgetedValue,
                                                                                                      dayValue);
                                                                                      db.collection("users")
                                                                                              .document(username)
                                                                                              .collection("weeklyExpenses")
                                                                                              .document("week " + weekNumberValue)
                                                                                              .collection("expenses")
                                                                                              .document("expense " + expenseNumberValue)
                                                                                              .set(dbLogExpense)
                                                                                              .addOnCompleteListener(new OnCompleteListener<Void>() {
                                                                                                  @Override
                                                                                                  public void onComplete(@NonNull Task<Void> task) {
                                                                                                      if (task.isSuccessful())
                                                                                                      {
                                                                                                          Toast.makeText(getApplicationContext(), "Your expense has been logged", Toast.LENGTH_SHORT).show();

                                                                                                      }
                                                                                                      else
                                                                                                      {
                                                                                                          Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
                                                                                                      }
                                                                                                  }
                                                                                              });


                                                                                  }
                                                                              })
                                                                              .addOnFailureListener(new OnFailureListener() {
                                                                                  @Override
                                                                                  public void onFailure(@NonNull Exception e) {
                                                                                      Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
                                                                                  }
                                                                              });
                                                                      }
                                                                  }
                                                                  }
                                                              });
                                                           }
                                                       }
                                                       else
                                                       {
                                                        // database error
                                                           Toast.makeText(getApplicationContext(), "Database error! Try again later", Toast.LENGTH_SHORT).show();
                                                       }
                                                   }
                                               });
                                           }
                                           else
                                           {

                                           }
                                       }
                                   });

                               }
                           }
                           else
                           {
                               Toast.makeText(getApplicationContext(), "Sorry, there has been a database error. Please try again later", Toast.LENGTH_SHORT).show();
                           }

                        }
                    });
                }


            }
        });







    }
}
package com.example.contactmanager;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.material.textfield.TextInputEditText;
import com.vishnusivadas.advanced_httpurlconnection.FetchData;
import com.vishnusivadas.advanced_httpurlconnection.PutData;


public class SignIn extends AppCompatActivity {

    Button signUp;
    Button login;
    EditText textInputFullname, textInputUsername, textInputEmail, textInputPassword;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_in);

        signUp = findViewById(R.id.creation);
        login = findViewById(R.id.login);

        textInputEmail = findViewById(R.id.email);
        textInputFullname = findViewById(R.id.fname);
        textInputPassword = findViewById(R.id.pw);
        textInputUsername = findViewById(R.id.uname);

        signUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String fullname;
                String username;
                String email;
                String password;

                fullname = String.valueOf(textInputFullname.getText());
                username = String.valueOf(textInputUsername.getText());
                email = String.valueOf(textInputEmail.getText());
                password = String.valueOf(textInputPassword.getText());

                if(!fullname.equals("") && !username.equals("") && !email.equals("") && !password.equals("")) {

                    //Start ProgressBar first (Set visibility VISIBLE)
                    Handler handler = new Handler(Looper.getMainLooper());
                    handler.post(new Runnable() {
                        @Override
                        public void run() {
                            //Starting Write and Read data with URL
                            //Creating array for parameters
                            String[] field = new String[4];
                            field[0] = "fullname";
                            field[1] = "username";
                            field[2] = "email";
                            field[3] = "password";
                            //Creating array for data
                            String[] data = new String[4];
                            data[0] = fullname;
                            data[1] = username;
                            data[2] = email;
                            data[3] = password;

                            PutData putData = new PutData("http://10.0.0.95/LoginRegister/signup.php", "POST", field, data);
                            if (putData.startPut()) {
                                if (putData.onComplete()) {
                                    String result = putData.getResult();
                                    if (result.equals("Sign Up Success"))
                                    {
                                        Toast.makeText(getApplicationContext(), result, Toast.LENGTH_SHORT).show();
                                        openHomescreen();
                                        finish();
                                    }
                                    else
                                    {
                                        Toast.makeText(getApplicationContext(), result, Toast.LENGTH_SHORT).show();
                                    }
                                }
                            }
                            //End Write and Read data with URL
                        }
                    });
                }

                else
                {
                    Toast.makeText(getApplicationContext(), "All fields are required", Toast.LENGTH_SHORT).show();
                }

            }
        });

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                LoginScreen();
            }
        });




    }
    public void LoginScreen()
    {
        Intent intent = new Intent(this, Login.class);
        startActivity(intent);
    }
    public void openHomescreen()
    {
        Intent intent = new Intent(this, Homescreen.class);
        startActivity(intent);
    }
}
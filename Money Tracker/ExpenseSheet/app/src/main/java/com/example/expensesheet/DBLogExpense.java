package com.example.expensesheet;

import android.widget.EditText;

public class DBLogExpense {


    public String amountSpent, category, description, moneyBudgeted, day;

    public DBLogExpense(String amountspent, String category, String description, String moneyBudgeted, String day)
    {
        this.amountSpent = amountspent;
        this.category = category;
        this.description = description;
        this.moneyBudgeted = moneyBudgeted;
        this.day = day;

    }

    public String getAmountSpent() {return amountSpent;}

    public void setAmountSpent(String amountSpent) {
        this.amountSpent = amountSpent;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getMoneyBudgeted() {
        return moneyBudgeted;
    }

    public void setMoneyBudgeted(String moneyBudgeted) {this.moneyBudgeted = moneyBudgeted;}

    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }


}

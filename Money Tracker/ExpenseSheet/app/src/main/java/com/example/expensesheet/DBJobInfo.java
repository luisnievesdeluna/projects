package com.example.expensesheet;

public class DBJobInfo {
    public String jobtitle, salary, type;

    public DBJobInfo(String jobtitle, String salary, String type)
    {
        this.jobtitle = jobtitle;
        this.salary = salary;
        this.type = type;
    }

    public String getJobtitle() {
        return jobtitle;
    }

    public void setJobtitle(String jobtitle) {
        this.jobtitle = jobtitle;
    }

    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }

    public String getType(){return type;}

    public void setType(String type){this.type = type;}

    public DBJobInfo(){}
}

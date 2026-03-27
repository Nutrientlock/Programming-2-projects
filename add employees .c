//Author: Ajay Clarke 
// Date: N/A 
// Description: Group Project (Add Employee)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


// Open File 
FILE *open_file();

// Close File
void close_file(FILE *file);

// function to appeand of create a new file
void Clean_file (struct employee *emp);

// Function to add Employee
void Add_Employee(struct employee *emp);

// Validate the uniqueness of ID number
int valid_id (char * idPtr);

// validate employee status
int Valid_status(char *status); 

// validate employee role
int Valid_role(char *role);

// list Employees
void list_emplyees(struct employee *emp);

// Find Employee
void find_employee(struct employee *emp);

//Update Record
void Update_Record(struct employee *emp);


#define CSV_file "C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv"

// struct to receive Employee data
struct employee{
    char Employee_ID [10];
    char First_name [40];
    char Last_name [40];
    char Role [40];
    char Status [40];
    int Hourly_rate;
};
struct employee emp;


int main(){
    struct employee *empPtr = &emp;

    FILE *file = open_file();
    if (file == NULL) return 1;


    list_emplyees(empPtr);
    close_file(file);
    find_employee(empPtr);

    return 0;
}

FILE *open_file(){
    FILE *file;
    file = fopen(CSV_file, "a");
    if (file == NULL){
        printf("File failed to open");
        return NULL;
    }

    else {
        printf ("file open successful\n");
        Clean_file(&emp);
        return file;
    }
}

void close_file(FILE* file){
     fclose(file);
}

// function to appeand of create a new file
void Clean_file(struct employee *emp){
    int clean_file;

    printf("Do you want a clean Document 1 for no and 0 for yes: ");
    scanf("%d", &clean_file);

    if (clean_file == 0){
        FILE *file = fopen(CSV_file, "w"); 
        fclose(file);
        Add_Employee(emp);
    }
    else if (clean_file == 1){
        Add_Employee(emp);
    }
    else {
        printf("Invalid Input");
    }
}

// Validate the uniqueness of ID number
int valid_id(char *idPtr) {
    char existingID[10];
    char line[200];

    FILE *file = fopen(CSV_file, "r");
    if (file == NULL) {
        return 0; 
    }

    while (fgets(line, sizeof(line), file) != NULL) {
       
        sscanf(line, "%[^,]", existingID); 

        if (strcmp(existingID, idPtr) == 0) {
            fclose(file);
            return 1; 
        }
    }

    close_file(file);
    return 0;
}

// validate employee status
int Valid_status(char *Status){
    int i = 0;
    while (Status[i] != '\0'){
        Status [i] = toupper(Status[i]);
        i += 1;
    }
    if (strcmp(Status, "ACTIVE") == 0)     return 1;
    if (strcmp(Status, "LEAVE") == 0)      return 1;
    if (strcmp(Status, "TERMINATED") == 0) return 1;

    printf("Invalid Input");
    return 0;

}

// Validate employee role
int Valid_role(char *role){
    int i =0;
    char temp[40] = {0};

    while (temp [i] != '\n'){ 
    temp [i] = role [i];
    i ++;
    }

    while (temp[i] !='\0' ){
        temp[i] = toupper(temp[i]);
        i++;
    }
    if (strcmp(temp, "MANAGER") == 0)    return 1;
    if (strcmp(temp, "DEVELOPER") == 0)  return 1;
    if (strcmp(temp, "ANALYST") == 0)    return 1;
    if (strcmp(temp, "HR") == 0)         return 1;
    if (strcmp(temp, "ADMIN") == 0)      return 1;
    if (strcmp(temp, "ENGINEER") == 0)   return 1;
    if (strcmp(temp, "INTERN") == 0)     return 1;

    printf("Invalid Role");
    return 0;
}

// Function to add Employee
void Add_Employee(struct employee *emp){

    struct employee local_emp;
    int starter = 0;
    char *idPtr = NULL;
    int validate ;

    do {
        printf("Press 1 Add Employee or -999 to stop: ");
        scanf("%d", &starter);

        if (starter > 1 || starter <= 0){
            break;
        }


        printf("Enter Employee ID,\nmust be 10 characters: ");
        scanf("%s", emp->Employee_ID);

        idPtr= emp->Employee_ID; 

        if (strlen(emp->Employee_ID) <= 10){

            if (valid_id(emp->Employee_ID) == 1) { 
                printf("Error: ID already exists. Try a different ID.\n");
                continue; 
            }

            printf("Enter Employee First name: ");
            scanf("%s", emp->First_name);

            printf("Enter Employee Last name: ");
            scanf("%s", emp->Last_name);

            do{
            printf("Enter Employee Role (Manager, Developer, Analyst, HR, Admin, Engineer, Intern): ");
            scanf("%s", emp->Role);
            } while(Valid_role (emp->Role) == 0);

            do {
            printf("Enter Employee, Status Active, on leave, or terminated: ");
            scanf("%s", emp->Status);
            
                if (Valid_status(emp->Status) == 0){
                    printf("\nError: Invalid Status. Must be Active, On Leave, or Terminated: \n");
                
                }
            }
            while(Valid_status(emp->Status) == 0);

            printf("Enter employee Hourly rate");
            scanf("%d",&emp->Hourly_rate);

            FILE *file = fopen(CSV_file, "a"); 

            if (file == NULL) {
                printf("File Failed to open\n");
                return; 
            }

            fprintf(file, "%s,%s,%s,%s,%s,%d\n",  
                emp->Employee_ID,
                emp->First_name,
                emp->Last_name,
                emp->Role,
                emp->Status,
                emp->Hourly_rate
            );

            fclose(file);
            printf("Employee added successfully.\n");

        }
        else {
            printf("ID Number is Invalid");
        }

}   while(starter != -999);
}

// list Employees
void list_emplyees(struct employee *emp){

    char Employee_ID[10];
    char First_name[40];
    char Last_name[40];
    char Role[40];
    char Status[40];
    char line[200];
    int hourly_rate;
    char Full_name[80];

    FILE *file = fopen(CSV_file, "r");
    
    if (file == NULL) {
        printf("Error: Employee file not found.\n");
        return;
    }

    fseek(file, 0, SEEK_END);
    long int size = ftell(file);

    if (size == 0) {
        printf("No employees found. File is empty.\n");
        fclose(file);
        return;
    }

    rewind(file);

    // print table header
    printf("\n%-10s %-20s %-20s %-15s %-15d\n",
        "ID", "Full Name", "Role", "Status", "hourly rate");
    printf("--------------------------------------------------------------\n");

    while (fgets(line, sizeof(line), file) != NULL) {
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^\n]",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        // combine first and last name
       
        snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

        printf("%-10s %-20s %-20s %-15s %-15d\n",
            emp->Employee_ID,
            Full_name,
            emp->Role,
            emp->Status,
            emp->Hourly_rate);
    }

    printf("--------------------------------------------------------------\n");
    close_file(file);
}


// find_employee
void find_employee(struct employee *emp){

    char line [200];
    char ID_search [10];
    char ID_in_system[10];
    char Full_name[80];
   
    

    printf("Enter the ID number of the person you wish to find: ");
    scanf("%s",ID_search);

    FILE *file = fopen(CSV_file, "r");
    
    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,]", ID_in_system); 
        if (strcmp(ID_in_system, ID_search) == 0 ){

            printf("\n%-10s %-20s %-20s %-15s %-15d\n", "ID", "Full Name", "Role", "Status", "Hourly Rate");
            printf("--------------------------------------------------------------\n");
                sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^\n]",
                    emp->Employee_ID,
                    emp->First_name,
                    emp->Last_name,
                    emp->Role,
                    emp->Status,
                    emp->Hourly_rate);

                // combine first and last name
                snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

                printf("%-10s %-20s %-20s %-15s %-15d\n",
                    emp->Employee_ID,
                    Full_name,
                    emp->Role,
                    emp->Status,
                    emp->Hourly_rate);
            
            printf("--------------------------------------------------------------\n");
            close_file(file);


        }
    }
}
// Update Record
void Update_Record(struct employee *emp){
    char line [200];
    char ID_search [10];
    char ID_in_system[10];
    
    printf("Enter the ID number of the record you wish to update: ");
    scanf("%s",ID_search);

    FILE *file = fopen("CSV_file", "r");
    
    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,]", ID_in_system); 
        if (strcmp(ID_in_system, ID_search) == 0 ){
            
        }
    }

}

//Author: Ajay Clarke 
// Date: N/A 
// Description: Group Project (Add Employee)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define CSV_file "C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv"
#define TEMP_file "C:\\Users\\ajayc\\Desktop\\P2\\temp.csv"

// struct to receive Employee data
struct employee{
    char Employee_ID [10];
    char First_name [40];
    char Last_name [40];
    char Role [40];
    char Status [40];
    float Hourly_rate;
};
struct employee emp;

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
// Delete Record
void Delete_Record(struct employee *emp);


int main(){
    struct employee *empPtr = &emp;

    
    FILE *file = open_file();
    if (file == NULL) return 1;

    list_emplyees(empPtr);
    close_file(file);
    find_employee(empPtr);
    Update_Record(empPtr);
    Delete_Record(empPtr);
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
    close_file(file);
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
    char temp[40];

    strncpy(temp, role, sizeof(temp) - 1);
    temp[sizeof(temp) - 1] = '\0';

    while (temp[i] !='\n' ){
        temp[i] = toupper(temp[i]);
        i++;
    }
    if (strcmp(temp, "MANAGER") == 0)    return 1;
    if (strcmp(temp, "SERVER") == 0)  return 1;
    if (strcmp(temp, "COOK") == 0)    return 1;
    if (strcmp(temp, "CASHIER") == 0)         return 1;
    if (strcmp(temp, "HUMAN RESOURCES") == 0)  return 1;
    if (strcmp(temp, "ADMIN") == 0)      return 1;
    if (strcmp(temp, "ENGINEER") == 0)   return 1;
    if (strcmp(temp, "INTERN") == 0)     return 1;

    return 0;
}

// Function to add Employee
void Add_Employee(struct employee *emp){
    int starter = 0;


    do {
        printf("Press 1 Add Employee or -999 to stop: ");
        scanf("%d", &starter);

        if (starter > 1 || starter <= 0){
            break;
        }

        printf("Enter Employee ID,\nmust be 10 characters: ");
        scanf("%s", emp->Employee_ID);

        if (strlen(emp->Employee_ID) <= 10){
            printf("ID Number is Valid\n");
            continue;;
        }

        if (valid_id(emp->Employee_ID) == 1) { 
            printf("Error: ID already exists. Try a different ID.\n");
            continue; 
        }

        printf("Enter Employee First name: ");
        scanf("%s", emp->First_name);

        printf("Enter Employee Last name: ");
        scanf("%s", emp->Last_name);

        do{
        printf("Enter Employee Role (MANAGER, SERVER, COOK, CASHIER, HUMAN RESOURCES, ADMIN, ENGINEER, INTERN):");
        scanf("%s", emp->Role);
        if (Valid_role(emp->Role) == 0){
            printf("Invalid Role. Please try again.\n");
        }
        } while(Valid_role (emp->Role) == 0);

        do {
            printf("Enter Employee, Status Active, on leave, or terminated: ");
            scanf("%s", emp->Status);
            if (Valid_status(emp->Status) == 0){
            printf("\nError: Invalid Status. Must be Active, On Leave, or Terminated: \n");
            }
        }while(Valid_status(emp->Status) == 0);

        do{
            printf("Enter Employee Hourly Rate: ");
            scanf("%f", &emp->Hourly_rate);
            if (emp->Hourly_rate < 0 || emp->Hourly_rate > 80){
                printf("Invalid Hourly Rate. Must be a positive integer between 0 and 80.\n");
            }
        } while (emp->Hourly_rate < 0 || emp->Hourly_rate > 80);


        FILE *file = fopen(CSV_file, "a"); 

        if (file == NULL) {
            printf("File Failed to open\n");
            return; 
        }

        fprintf(file, "%s,%s,%s,%s,%s,%.2f\n",  
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            emp->Hourly_rate
        );

        fclose(file);
        printf("Employee added successfully.\n");
        }while(starter != -999);
    } 

// list Employees
void list_emplyees(struct employee *emp){
    char line[200];
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
    printf("\n%-10s %-20s %-20s %-15s %-15s\n",
        "ID", "Full Name", "Role", "Status", "Hourly Rate");
    printf("--------------------------------------------------------------------------------\n");

    while (fgets(line, sizeof(line), file) != NULL) {
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%f",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        // combine first and last name
        snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

        printf("%-10s %-20s %-20s %-15s %-15.2f\n",
            emp->Employee_ID,
            Full_name,
            emp->Role,
            emp->Status,
            emp->Hourly_rate);
    }

    printf("--------------------------------------------------------------------------------\n");
    close_file(file);
}


// find_employee
void find_employee(struct employee *emp){
    char line [200];
    char ID_search [10];
    char ID_in_system[10];
    char Full_name[80];
    int found = 0;
   
    printf("Enter the ID number of the person you wish to find: ");
    scanf("%s",ID_search);

    FILE *file = fopen(CSV_file, "r");
    if (file == NULL) {                          // FIX 2a
        printf("Error: Employee file not found.\n");
        return;
    }

    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,]", ID_in_system); 

        if (strcmp(ID_in_system, ID_search) == 0 ){
            found = 1;

                sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%f",
                    emp->Employee_ID,
                    emp->First_name,
                    emp->Last_name,
                    emp->Role,
                    emp->Status,
                    &emp->Hourly_rate);

                // combine first and last name
                snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);
               
                printf("\n%-10s %-20s %-20s %-15s %-15s\n", "ID", "Full Name", "Role", "Status", "Hourly Rate");
                printf("--------------------------------------------------------------\n");
                printf("%-10s %-20s %-20s %-15s %-15.2f\n",
                    emp->Employee_ID,
                    Full_name,
                    emp->Role,
                    emp->Status,
                    emp->Hourly_rate);
            
            printf("--------------------------------------------------------------\n");
            break;
        }
    }

    if (found == 0)
        printf("Employee with ID '%s' not found.\n", ID_search);

    fclose(file);
}

// Update Record
void Update_Record(struct employee *emp){
    char line [200];
    char ID_search [10];
    int found = 0;
    int choice;
    
    printf("Enter the ID number of the record you wish to update: ");
    scanf("%s",ID_search);

    FILE *file = fopen(CSV_file, "r");
    if (file == NULL) {
        printf("Error: Employee file not found.\n");
        return;
    }

     FILE *temp = fopen(TEMP_file, "w");
    if (temp == NULL) {
        printf("Error: Could not create temp file.\n");
        fclose(file);
        return;
    }

    while (fgets(line, sizeof(line), file) != NULL) {
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%f",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        if (strcmp(emp->Employee_ID, ID_search) == 0) {
            found = 1;

            printf("Found: %s %s %s, Role: %s, Status: %s, Hourly Rate: %.2f\n",
                emp->Employee_ID,
                emp->First_name,
                emp->Last_name,
                emp->Role,
                emp->Status,
                emp->Hourly_rate);

            do {
                printf("What would you like to update?\n");
                printf("1. First Name\n2. Last Name\n3. Role\n4. Status\n5. Hourly Rate\n6. Stop updating\n");
                printf("Enter your choice: ");
                scanf("%d", &choice);

                switch(choice){
                    case 1:
                        printf("Enter new First Name: ");
                        scanf("%s", emp->First_name);
                        continue;
                    case 2:
                        printf("Enter new Last Name: ");
                        scanf("%s", emp->Last_name);
                        continue;
                    case 3:
                        do { 
                            printf("Enter new Role (MANAGER, SERVER, COOK, CASHIER, HUMAN RESOURCES, ADMIN, ENGINEER, INTERN): ");
                            scanf("%s", emp->Role);
                            if (Valid_role(emp->Role) == 0){
                                printf("Invalid Role. Please try again.\n");
                            }
                        } while (Valid_role(emp->Role) == 0);
                        continue;
                    case 4:
                        do {
                            printf("Enter new Status (ACTIVE, LEAVE, TERMINATED): ");
                            scanf("%s", emp->Status);
                            if (Valid_status(emp->Status) == 0){
                                printf("Invalid Status. Please try again.\n");
                            }
                        } while (Valid_status(emp->Status) == 0);
                        continue;
                    case 5:
                        do {
                            printf("Enter new Hourly Rate: ");
                            scanf("%f", &emp->Hourly_rate);
                            if (emp->Hourly_rate < 0 || emp->Hourly_rate > 80){
                                printf("Invalid Hourly Rate. Must be a positive integer between 0 and 80.\n");
                            }
                        } while (emp->Hourly_rate < 0 || emp->Hourly_rate > 80);
                        continue;
                    default:
                        printf("Invalid choice. Please try again.\n");
                }
            } while(choice < 1 || choice > 5);
        }

        fprintf(temp, "%s,%s,%s,%s,%s,%.2f\n",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            emp->Hourly_rate);
    }
    fclose(file);
    fclose(temp);

    if (found == 0) {
        printf("Employee with ID '%s' not found.\n", ID_search);
        remove(TEMP_file);
        return;
    }

    remove(CSV_file);
    rename(TEMP_file, CSV_file);
    printf("Employee updated successfully.\n");
}

// Delete Record 
void Delete_Record(struct employee *emp){
    char line [200];
    char ID_search [10];


    FILE *file = fopen(CSV_file, "r");
        if (file == NULL) {
            printf("Error: Employee file not found.\n");
            return;
        }

    FILE *temp = fopen(TEMP_file, "w");
        if (temp == NULL) {
            printf("Error: Could not create temp file.\n");
            fclose(file);
            return;
        }
    
    printf("Enter the ID number of the record you wish to delete: ");
    scanf("%s",ID_search);

    while(fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%f",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        if (strcmp(emp->Employee_ID, ID_search) != 0){
            fprintf(temp, "%s,%s,%s,%s,%s,%.2f\n",
                emp->Employee_ID,
                emp->First_name,
                emp->Last_name,
                emp->Role,
                emp->Status,
                emp->Hourly_rate);
        }

    } 
    fclose(file);
    fclose(temp);

    remove(CSV_file);
    rename(TEMP_file, CSV_file);
    printf("Employee with ID '%s' deleted successfully.\n", ID_search);
}


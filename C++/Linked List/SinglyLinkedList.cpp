#include<iostream>
#include<conio.h>
#include<cstdlib>

using namespace std;

class list
{
    int data;
    list *next;
public:
    void insert_end();
    void insert_front();
    void display();
    void delete_specific();
    void delete_front();
    void delete_end();
    int length();
};

list *head = nullptr;
list *curr = nullptr;

void list :: insert_end()
{
    list *temp = new list();
    cout<<"Enter Data : ";
    cin>>temp->data;
    temp->next = nullptr;

    if (head == nullptr)
        {
            head = temp;
        }
    else
        {
            for (curr = head ; curr->next != nullptr ; curr = curr->next);
            curr->next = temp;
        }
}
void list :: insert_front()
{
    list *temp = new list();

    cout<<"Enter Data : ";
    cin>>temp->data;

    temp->next = nullptr;

    if( head == nullptr)
        head = temp;
    else
        {
            temp->next = head;
            head = temp;
        }
}
void list :: display()
{
    if(head == nullptr)
        cout <<"Empty List !";
    else
        {
            curr = nullptr;
            cout<<" ";
            for (curr = head ; curr->next != nullptr ; curr = curr->next)
            {
                cout<<curr->data<<"-->";
            }
            cout<<curr->data<<endl;
        }
}
void list :: delete_end()
{
    if ( head == nullptr)
        cout<<"List is already empty !"<<endl;
    else if(head->next == nullptr)
    {
        int p = head->data;
        head = nullptr;
        cout<<"Deleted Element is : "<<p<<endl;
    }
    else
        {
            for (curr = head ; curr->next->next != nullptr ; curr = curr->next);
                int x = curr->next->data;
                curr->next= nullptr;
                cout <<"Deleted Element is : "<<x <<endl;
        }
}
void list :: delete_front()
{
    if ( head == nullptr)
        cout<<"List is already empty !"<<endl;
    else
        {
            int x = head->data;
            head = head->next;
            cout<<"Deleted Element is : "<<x<<endl;
        }
}

void list :: delete_specific()
{
   if(head == nullptr)
   {
       cout<<"List is empty !" ;
   }
   else
   {
       cout<<"Enter the value to be deleted : ";
       int e ;
       cin>>e;
       if(head->data == e)
            {
                delete_front();
            }
       else
       {
           list *prev;
         for(curr = head ; curr->data != e && curr->next != nullptr ; prev = curr , curr = curr->next);
        if(curr->next == nullptr)
            {
                if(curr->data == e)
                {
                     prev->next = curr->next;
                    delete curr ;
                    cout<<"Value deleted ! "<<endl;
                }
                else cout<<"Element Not Found ! "<<endl;
            }
         else
            {
                prev->next = curr->next;
                delete curr ;
                cout<<"Value deleted ! "<<endl;
            }
       }
    }
}

int list ::  length()
{
    int x = 0;
    if(head == nullptr)
        return 0;
    else
        {
            for(curr = head ; curr->next != nullptr ; curr = curr->next)
                    x++;
            return x+1;
        }

}
int main()
{
    list a;
    int l;
        a.insert_end();
        a.insert_end();
        a.insert_end();

        a.display();

        a.insert_front();
        a.insert_front();
        a.insert_front();

        a.display();
        l = a.length();
        cout<<"Length  = " << l <<endl;
        a.delete_front();
        a.display();

        a.delete_end();
        a.display();

        a.delete_specific();
        a.display();

         l = a.length();
        cout<<"Length  = " << l <<endl;
    return 0;
}

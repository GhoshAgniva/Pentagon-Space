print(''' 
               MENU
    --------------------------------

    1.IDLY -  30      4.ANNA SAMBAR - 50
    2.RICE BATH - 40  5.TEA - 15
    3.BADA -   30     6.COFFEE - 15
    ----------------------------------  
      ''')


def idly_bill():
    num_idly = int(input("Enter the number of idly you want: "))
    original_cost=num_idly*30
    gst_amount = (original_cost * 18) / 100
    total_cost = gst_amount+original_cost

    print(f''' 
                  Cafe name
    --------------------------------------------------    
    Bill no -01               Date-24/04/2024
    Food item       Qyn                 Cost
       IDLY        {num_idly}\t\t      {original_cost}                                                                                                                                                           
    ---------------------------------------------------
    18% GST                              {gst_amount}
    -------------------------------------------------------
    Total Amount                          {total_cost}
       ''')




def rice_bath_bill():
    num_rice_bath = int(input("Enter the number of Rice Bath you want: "))
    original_cost=num_rice_bath*40
    gst_amount = (original_cost * 18) / 100
    total_cost = gst_amount+original_cost
    print(f''' 
                    Cafe name
      --------------------------------------------------    
      Bill no -01                        Date-24/04/2024
      Food item            Qyn                       Cost
      Rice Bath        {num_rice_bath}\t\t      {original_cost}                                                                                                                                                           
      ---------------------------------------------------
      18% GST                              {gst_amount}
      -------------------------------------------------------
      Total Amount                          {total_cost}
         ''')


def bada_bill():
    num_bada = int(input("Enter the number of Bada you want: "))
    original_cost=num_bada*30
    gst_amount = (original_cost * 18) / 100
    total_cost = gst_amount+original_cost
    print(f''' 
                    Cafe name
      --------------------------------------------------    
      Bill no -01               Date-24/04/2024
      Food item       Qyn                 Cost
        Bada        {num_bada}\t\t      {original_cost}                                                                                                                                                           
      ---------------------------------------------------
      18% GST                              {gst_amount}
      -------------------------------------------------------
      Total Amount                          {total_cost}
         ''')



def anna_sambar_bill():
    num_anna_sambar = int(input("Enter the number of Anna Sambar you want: "))
    original_cost=num_anna_sambar*50
    gst_amount = (original_cost * 18) / 100
    total_cost = gst_amount+original_cost
    print(f''' 
                    Cafe name
      --------------------------------------------------    
      Bill no -01               Date-24/04/2024
      Food item       Qyn                 Cost
         IDLY        {num_anna_sambar}\t\t      {original_cost}                                                                                                                                                           
      ---------------------------------------------------
      18% GST                              {gst_amount}
      -------------------------------------------------------
      Total Amount                          {total_cost}
         ''')



selected_menu = input("Enter a menu:")

if selected_menu.lower() .strip()== "idly":
    idly_bill()

elif selected_menu.lower().strip()== "riceBath":
    rice_bath_bill()

elif selected_menu.lower().strip() == "anna sambar":
    anna_sambar_bill()

elif selected_menu.lower().strip() == "bada":
    bada_bill()


# Ebidding Readme file
1) The Auction System (AS) resides in the cloud for scalability and elasticity purpose.
2) The AS allows for the end-users to register.
3) At registration time, end-users might select the option of being notified by voice when selected events happen
      (e.g. end-users registering /leaving, new items put on sale, items sold).
4) Only registered end-users are allowed to offer items for auction and bid.
5) A registered enduser can advertise many items for sale at a time. Auctions for an item are open during a
     specified period of time after its advertising and the broadcasting of the information to all registered end-users.
6) An item is sold to the highest bid at the end of the specified period of time.
7) For every item, the AS keeps informing the end-users about the current highest bid.
8) An end-user can bid as many times as she/he wishes for an item on auction.

#Constraints

9) An end-user has a unique Name.
10) The AS has to keep this information.
11) An end-user can always try to leave the Auction System. However, she/he can be denied deregistration if
she/he is currently offering an item for auction or active in bidding for at least one item
(currently leading with the highest bid for at least one item).
12) Every registered end-user can offer items for sale
13) An end-user can bid on any item being currently offered and can submit as many items as
she/he wishes.
14) To keep the end-users informed on every item, any change in the current highest bid is sent to all the registered end-users.
15) When the bidding period  is over, the AS informs the winning users.
16) If there is more than one end-user with the highest bid, the first bid to reach the AS wins.
17) The AS also informs the end-user who is selling the item about the winner.
18) When an item has not attracted a single valid bid, the AS restarts the bidding process for another period of time.
     This can be repeated until an end-user makes a winning bid.

     Bid start
     Bid end ==> eventHandler()
       if (bid.exists?){
         announcer= winner and close
       }else{
         restart bid
       }

#Have to Completed:

3
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './components/Home';
import CakeList from './components/CakeList';
import CakeDetails from './components/CakeDetails';
import ShoppingCart from './components/ShoppingCart';
import Checkout from './components/Checkout';
import AccountDashboard from './components/AccountDashboard';
import AdminDashboard from './components/AdminDashboard';
import AdminOrderDetails from './components/AdminOrderDetails';
import AdminUsers from './components/AdminUsers';
import AddCake from './components/AddCake';
import EditCakes from './components/EditCakes';

const App = () => {
  return (
    <Router>
      <div className="container mx-auto p-4">
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/cakes" component={CakeList} />
          <Route path="/cakes/:id" component={CakeDetails} />
          <Route path="/cart" component={ShoppingCart} />
          <Route path="/checkout" component={Checkout} />
          <Route path="/account" component={AccountDashboard} />
          <Route path="/admin" exact component={AdminDashboard} />
          <Route path="/admin/orders/:id" component={AdminOrderDetails} />
          <Route path="/admin/users" component={AdminUsers} />
          <Route path="/admin/cakes/add" component={AddCake} />
          <Route path="/admin/cakes/edit/:id" component={EditCakes} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
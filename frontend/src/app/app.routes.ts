import { Routes } from '@angular/router';

import { ProductRegistrationComponent } from './components/product-registration/product-registration.component';
import { InventoryDeliveryComponent } from './components/inventory-delivery/inventory-delivery.component';

export const appRoutes: Routes = [
   { path: 'register', component: ProductRegistrationComponent },
   { path: 'deliver', component: InventoryDeliveryComponent },
   { path: '', redirectTo: '/register', pathMatch: 'full' }
];

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { InventoryService } from '../../services/inventory.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-registration',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './product-registration.component.html',
  styleUrl: './product-registration.component.css'
})
export class ProductRegistrationComponent implements OnInit {

  productTypes: any[] = [];
  productForm: FormGroup;

  constructor(private fb: FormBuilder, private inventoryService: InventoryService) {
    this.productForm = this.fb.group({
      selectedProduct: ['', Validators.required],
      serialNumber: ['', Validators.required],
      deliveryDate: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.loadProductTypes();
  }

  loadProductTypes(): void {
    this.inventoryService.getProductTypes().subscribe(data => {
      console.log("PRODUCTS: " + JSON.stringify(data));
      this.productTypes = data;
    });
  }

  saveInventory(): void {
    if (this.productForm.valid) {
      const newInventoryItem = {
        product_type_id: this.productForm.get('selectedProduct')?.value,
        numero_serie: this.productForm.get('serialNumber')?.value,
        delivery_date: this.productForm.get('deliveryDate')?.value,
        status: 'Pending'
      };

      this.inventoryService.addInventoryItem(newInventoryItem).subscribe(() => {
        this.productForm.reset();
      });
    }
  }
}

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
      username: ['', Validators.required],
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
        usuario: this.productForm.get('username')?.value,
        nombre_producto: this.productForm.get('selectedProduct')?.value,
        numero_serie: this.productForm.get('serialNumber')?.value,
        fecha_entrega: this.productForm.get('deliveryDate')?.value,
        status: 'Pendiente'
      };

      this.inventoryService.addInventoryItem(newInventoryItem).subscribe(() => {
        this.productForm.reset();
      });
    }
  }
}

import { Component, OnInit } from '@angular/core';
import { InventoryService } from '../../services/inventory.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-inventory-delivery',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './inventory-delivery.component.html',
  styleUrl: './inventory-delivery.component.css'
})
export class InventoryDeliveryComponent implements OnInit {

  inventoryItems: any[] = [];

  constructor(private inventoryService: InventoryService) { }

  ngOnInit(): void {
    this.loadInventory();
  }

  loadInventory(): void {
    this.inventoryService.getInventory().subscribe(data => {
      console.log("INVENTARIO: " + JSON.stringify(data));

      this.inventoryItems = data;
    });
  }

  deliverItem(item: any): void {
    if (item.status === 'Pending') {
      this.inventoryService.updateInventoryItem(item._id, { status: 'Delivered' }).subscribe(() => {
        this.loadInventory();
      });
    }
  }
}
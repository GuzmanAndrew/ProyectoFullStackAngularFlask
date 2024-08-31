import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InventoryDeliveryComponent } from './inventory-delivery.component';

describe('InventoryDeliveryComponent', () => {
  let component: InventoryDeliveryComponent;
  let fixture: ComponentFixture<InventoryDeliveryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InventoryDeliveryComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InventoryDeliveryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

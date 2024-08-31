import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InventoryService {

  private apiUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) { }

  getProductTypes(): Observable<any> {
    return this.http.get(`${this.apiUrl}/product-types`);
  }

  addProductType(productType: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/product-types`, productType);
  }

  getInventory(): Observable<any> {
    return this.http.get(`${this.apiUrl}/inventory`);
  }

  addInventoryItem(item: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/inventory`, item);
  }

  updateInventoryItem(id: string, item: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/inventory/${id}`, item);
  }
}

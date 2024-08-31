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
    return this.http.get(`${this.apiUrl}/product-types/all`);
  }

  getInventory(): Observable<any> {
    return this.http.get(`${this.apiUrl}/inventory/all`);
  }

  addInventoryItem(item: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/inventory/create`, item);
  }

  updateInventoryItem(id: string, item: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/inventory/update/${id}`, item);
  }
}

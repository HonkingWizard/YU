import { Injectable } from '@angular/core';

import { AirQ } from '../../AirQ';
import { MockData } from '../../mock-airq';

/*
  Generated class for the DataFetchProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class DataFetchProvider {

  constructor() {
    console.log('Hello DataFetchProvider Provider');
  }

  getList(): AirQ[]{
    return MockData
  }


}

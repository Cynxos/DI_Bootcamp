import { Operation } from './Operation';

export class Addition implements Operation {
    public performOperation(a: number, b: number): number {
        return a + b;
    }
}
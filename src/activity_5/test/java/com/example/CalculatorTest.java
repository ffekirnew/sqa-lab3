package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    void testAdd() {
        assertEquals(5, calculator.add(2, 3), "2 + 3 should equal 5");
    }

    @Test
    void testSubtract() {
        assertEquals(1, calculator.subtract(4, 3), "4 - 3 should equal 1");
    }

    @Test
    void testMultiply() {
        assertEquals(12, calculator.multiply(3, 4), "3 * 4 should equal 12");
    }

    @Test
    void testDivide() {
        assertEquals(2.5, calculator.divide(5, 2), "5 / 2 should equal 2.5");
    }

    @Test
    void testDivideByZero() {
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(5, 0),
            "Division by zero should throw IllegalArgumentException");
    }

    @Test
    void testIsEven() {
        assertTrue(calculator.isEven(4), "4 should be even");
        assertFalse(calculator.isEven(5), "5 should not be even");
    }
}

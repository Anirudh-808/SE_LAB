import pytest
from coffee_shop_order import process_order_batch, check_espresso_machine

# Example test case:
def test_single_medium_coffee():
    orders = [
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "standard", "cost": 0.5}]
        }
    ]
    result = process_order_batch(orders, 0.1)
    assert result["total"] == 5.5
    assert result["status"] == "COMPLETED"

# TODO: Add test cases to achieve 90-100% on both Line and Branch coverage!
# test case 1
def test_unpaid_order():
    orders = [
        {
            "paid": False,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "standard", "cost": 0.5}]
        }
    ]
    result = process_order_batch(orders, 0.1)
    assert result["total"] == 0
    assert result["status"] == "NO_SALE"

# test case 2
def test_invalid_size():
    orders = [
        {
            "paid": True,
            "size": "extra_large",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "standard", "cost": 0.5}]
        }
    ]
    result = process_order_batch(orders, 0.1)
    assert result["total"] == 0
    assert result["status"] == "NO_SALE"

# test case 3
def test_strict_allergy_rejection():
    orders = [
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": True,
            "is_member": False,
            "customizations": [{"type": "allergen_alert", "cost": 0.0}]
        }
    ]
    result = process_order_batch(orders, 0.1)
    assert result["total"] == 0
    assert result["status"] == "NO_SALE"

# test case 4
def test_member_discount():
    orders = [
        {
            "paid": True,
            "size": "large",
            "strict_allergy": False,
            "is_member": True,
            "customizations": [{"type": "standard", "cost": 0.5}]
        }
    ]
    result = process_order_batch(orders, 0.1)
    assert result["total"] == 6.44
    assert result["status"] == "COMPLETED"

# test case 5
def test_rejected_items_audit():
    orders = [
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "allergen_alert", "cost": 0.0}]
        },
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "allergen_alert", "cost": 0.0}]
        },
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "allergen_alert", "cost": 0.0}]
        },
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "allergen_alert", "cost": 0.0}]
        },
        {
            "paid": True,
            "size": "medium",
            "strict_allergy": False,
            "is_member": False,
            "customizations": [{"type": "allergen_alert", "cost": 0.0}]
        }
    ]
    result = process_order_batch(orders, 0.1)
    assert result["total"] == 24.75
    assert result["status"] == "AUDIT_REJECTED"

# test case 6
def test_check_espresso_machine_no_data():
    result = check_espresso_machine([])
    assert result == "NO_DATA"

# test case 7
def test_check_espresso_machine_with_data():
    result = check_espresso_machine([[90, 95, 100], [85, 88, 92]])
    assert result == "OPTIMAL"

# test case 8
def test_check_espresso_machine_overheat():
    result = check_espresso_machine([[100, 105, 110]])
    assert result == "SHUTDOWN"
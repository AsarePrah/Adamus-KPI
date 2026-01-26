from Main import LeaveManagementApp
import os

def run_tests():
    app = LeaveManagementApp()
    # use a temp file for testing
    app.data_file = 'test_leave_data.json'
    # ensure clean start
    if os.path.exists(app.data_file):
        os.remove(app.data_file)

    # 1) Add employee
    ok = app.add_employee('E001', 'Alice', 'HR')
    assert ok, 'Failed to add employee'

    # 2) Apply for leave
    ok = app.apply_leave('E001', '2025-12-24', '2025-12-25', 'Annual')
    assert ok, 'Failed to apply leave'

    # 3) There should be one pending request
    assert len(app.leave_requests) >= 1, 'No leave requests recorded'
    idx = len(app.leave_requests) - 1
    assert app.leave_requests[idx]['status'] == 'Pending', 'Request not pending'

    # 4) Approve the leave
    ok = app.approve_leave(idx)
    assert ok, 'Failed to approve leave'
    assert app.leave_requests[idx]['status'] == 'Approved', 'Status not updated to Approved'

    # 5) Check leaves_used updated
    assert app.employees['E001']['leaves_used'] >= 1, 'Leaves used not updated'

    print('\nTESTS PASSED — All checks ok')

    # cleanup
    try:
        if os.path.exists(app.data_file):
            os.remove(app.data_file)
    except Exception:
        pass

if __name__ == '__main__':
    run_tests()

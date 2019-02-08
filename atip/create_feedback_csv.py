import csv
import atip.ease as e
import pytac

lattice = e.loader()
elements = e.preload(lattice)
elems = list(set(elements.hstrs + elements.vstrs + elements.bpms))
elems.sort(key=lambda x: x.index)
data = [("id", "field", "pv", "value"),
        (0, 'beam_current', 'SR-DI-DCCT-01:SIGNAL', 300),
        (0, 'feedback_status', 'CS-CS-MSTAT-01:FBSTAT', 0)]

for elem in elems:
    if 'HSTR' in elem.families:
        data.append((elem.index, 'error_sum',
                     elem.get_device('x_kick').name + ':ERCSUM', 0))
        data.append((elem.index, 'state',
                     elem.get_device('x_kick').name + ':STATE', 2))
        data.append((elem.index, 'h_fofb_disabled',
                     elem.get_pv_name('h_fofb_disabled', pytac.RB), 0))
        data.append((elem.index, 'h_sofb_disabled',
                     elem.get_pv_name('h_sofb_disabled', pytac.RB), 0))
    if 'VSTR' in elem.families:
        data.append((elem.index, 'error_sum',
                     elem.get_device('y_kick').name + ':ERCSUM', 0))
        data.append((elem.index, 'state',
                     elem.get_device('y_kick').name + ':STATE', 2))
        data.append((elem.index, 'v_fofb_disabled',
                     elem.get_pv_name('v_fofb_disabled', pytac.RB), 0))
        data.append((elem.index, 'v_sofb_disabled',
                     elem.get_pv_name('v_sofb_disabled', pytac.RB), 0))
    elif 'BPM' in elem.families:
        data.append((elem.index, 'enabled',
                     elem.get_pv_name('enabled', pytac.RB), 1))
        data.append((elem.index, 'x_fofb_disabled',
                     elem.get_pv_name('x_fofb_disabled', pytac.RB), 0))
        data.append((elem.index, 'x_sofb_disabled',
                     elem.get_pv_name('x_sofb_disabled', pytac.RB), 0))
        data.append((elem.index, 'y_fofb_disabled',
                     elem.get_pv_name('y_fofb_disabled', pytac.RB), 0))
        data.append((elem.index, 'y_sofb_disabled',
                     elem.get_pv_name('y_sofb_disabled', pytac.RB), 0))

with open("feedback.csv", "wb") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
function solve_time_to_mars()
    % Constants
    G = 6.6743*10^(-11);    % gravitational constant
    Mearth = 5.972*10^24;       % mass of Earth (kg)
    Mmars = 6.39*10^23;        % mass of Mars (kg)
    Rmars = 3.3895e6;          % radius of Mars (m)
    Rearth = 6371000;           % radius of Earth (m)
    d_earth_mars = 54.6e9;  % distance between Earth and Mars (m)
    Mejection = 2000;              % mass ejection rate (kg/s)
    Minitial = 100000;            % initial rocket mass (kg)
    Vejection = 50000;             % mass ejection velocity (m/s)
    
    % Function to calculate thrust at time t
    function thr = thrust(t)
        if t <= 35
            thr = Mejection*Vejection;
        else
            thr = 0;
        end
    end
    
    % Function to calculate mass of the rocket at time t
    function m = mass(t)
        if t <= 35
            m = Minitial - Mejection*t;
        else
            m = Minitial - Mejection*35;
        end
    end
    
    % ODE function for rocket dynamics
    function dydt = ode(t, y)
        r = y(1);
        v = y(2);
        m = mass(t);
        thr = thrust(t);
        % Acceleration
        acceleration = thr/m - G*Mearth/(r+Rearth)^2 + G*Mmars/(d_earth_mars-r+Rmars)^2;
        dydt = [v; acceleration];
    end
    
    % Event function to stop integration when r = d_earth_mars
    function [value, isterminal, direction] = event_function(t, y)
        value = y(1) - d_earth_mars;  % Stop when r = d_earth_mars
        isterminal = 1;  % Stop the integration
        direction = 0;   % All events
    end

    % Initial conditions
    y0 = [0; 0];
    tspan = [0 1000000]; % Time span for simulation
    
    % Solve the ODE with event function
    options = odeset('Events', @event_function); % Set event function
    [t, y, te, ye, ie] = ode45(@ode, tspan, y0, options);
    
    % Time when rocket reaches Mars
    time_to_mars = te(end); % Take the last event time as the rocket reaches Mars
    
    % Calculate position, velocity, and acceleration at time_to_mars
    r = ye(end, 1);
    v = ye(end, 2);
    m = mass(time_to_mars);
    thr = thrust(time_to_mars);
    acceleration = thr/m - G*Mearth/(r+Rearth)^2 + G*Mmars/(d_earth_mars-r+Rmars)^2;
    
    % Print information
    fprintf('Time to reach Mars: %.2f seconds\n', time_to_mars);
    fprintf('Position at Mars: %.2f meters\n', r);
    fprintf('Velocity at Mars: %.2f m/s\n', v);
    fprintf('Acceleration at Mars: %.2f m/s^2\n', acceleration);
end

% Call the function to solve for time to Mars and print information
solve_time_to_mars();
